import urllib, json, os
from datetime import datetime

def get_stats():
    #returns (viewers, followers, views)
    html = urllib.urlopen("https://api.twitch.tv/kraken/streams/" + "tipofthehats")
    data = json.loads(html.read())
    try:
        followers = data['stream']['channel']['followers']
    except:
        followers = -1
    try:
        viewers = data['stream']['viewers']
    except:
        viewers = -1
    try:
        views = data['stream']['channel']['views']
    except:
        views = -1
    return (viewers, followers, views)

#create file if not exist
filename = "_toth_data.txt"
if os.path.isfile(filename) == False:
    f = open(filename, 'w')
    f.write('date, viewers, followers, views, \n')
else:
    f = open(filename, 'a')

now = datetime.now()
time_format = "%H:%M:%S"
f.write(now.strftime(time_format) + ', ')
data = get_stats()
f.write(', '.join(str(datum) for datum in data) + ', \n')
f.close()

print "date, viewers, followers, views"
print now.strftime(time_format) + ', ' + ', '.join(str(datum) for datum in data)

