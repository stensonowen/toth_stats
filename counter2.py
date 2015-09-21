import sys, os

if len(sys.argv) != 2:
    print "Usage: " + sys.argv[0] + " <file>"
    exit(0)

f = open(sys.argv[1], 'r')

words = { "kids":0, "cancer":0, "rigged":0, "!pub":0, "lol":0 }
line_count = 0

for line in f:
    line_count += 1
    #word_count += line.upper().count(word)
    for word in words:
        words[word] += line.upper().count(word.upper())

#print word, "appeared", word_count, "times in", line_count, "lines"
print "Breakdown (out of", line_count, "lines:"
for i in words:
    print i, " \t ", words[i]


