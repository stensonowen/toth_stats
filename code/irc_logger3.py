#!/usr/bin/python
import sys, socket, time, re, urllib, json
from datetime import datetime, timedelta

#parse args
if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " <channelnel> + <log_file>"
    exit(0)
channel = sys.argv[1]
log_name = sys.argv[2]

t_period = timedelta(minutes = 1)

def parse_line(line):
    #attempts to parse a line into irc header and message content
    #if buffer was never full, will return tuple of user handle and message 
    #if line doesn't contain irc header (e.g. if buffer wasn't long enough 
        #and message was truncated), then will return blank handle
    if '!' not in line:
        return ('', line)
    handle = line[1:line.index('!')]
    prefix = ":%s!%s@%s.tmi.twitch.tv PRIVMSG #%s :" % (handle, handle, handle, channel)
    if prefix in line:
        message = line[len(prefix):]
        return (handle, message)
    else:
        return ('', line)
    
def check_stream_status():
    #returns bool indicating whether still streaming
    html = urllib.urlopen("https://api.twitch.tv/kraken/streams/" + channel)
    data = json.loads(html.read())
    return (data["stream"] != None)
	
#read logon creds
f = open("creds.txt", 'r')
nick = f.readline().strip()
pswd = f.readline().strip()

#connect to server
s=socket.socket()
s.connect(("irc.twitch.tv", 6667))
s.send("PASS %s\r\n" % pswd)
s.send("NICK %s\r\n" % nick)
s.send("JOIN #%s\r\n" % (channel))

#Verify logon creds
buffer = s.recv(1024)
if buffer == ":tmi.twitch.tv NOTICE * :Error logging in\r\n":
    print "Twitch rejected creds"
    exit(1)

#create temp vars
log_buf = handle = message = ""
time_format = "%H:%M:%S"
line_count = 0
t_start = t_lastcheck = datetime.now()
#open log
log = open(log_name, "w")
log.write("Log for twitch.tv/" + channel + ":\n")
log.write("Start: " + t_start.strftime(time_format) + "\n\n")

still_going = check_stream_status()

while still_going:
    time.sleep(.1)
    #retrieve messages
    #buffer helpful in long messages (mitigate truncations)
    buffer = buffer + s.recv(1024)
    messages = buffer.split('\n')
    buffer = messages.pop()
    t = datetime.now()

    for line in messages:
        log_buf = ""
        if line.split()[0] == 'PING':
            s.send('PONG %s\r\n' % line.split()[1])
            continue
        (handle, message) = parse_line(line)
        if(handle != ''):
            log_buf += t.strftime(time_format)
            log_buf += " " + handle + ": \t"
            log_buf += message + '\n'
        log.write(log_buf)
        line_count += 1
        #print line_count
        print line
        
	#check on channel if necessary
	if t - t_lastcheck >= t_period:
		t_lastcheck = t 
		still_going = check_stream_status()

#close file:
log.write("\nWrote " + str(line_count) + " lines. \n")
log.write("End: " + t.strftime(time_format) + "\n")
log.write("Time Elapsed: " + str(t - t_start) + "\n")
log.close()
