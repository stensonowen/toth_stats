import sys, os

if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " <file> <keyword>"
    exit(0)

f = open(sys.argv[1], 'r')

word = sys.argv[2].upper()
word_count = line_count = 0

for line in f:
    line_count += 1
    word_count += line.upper().count(word)

print word, "appeared", word_count, "times in", line_count, "lines"

