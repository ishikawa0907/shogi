#!/usr/bin/python

print "Content-type: text/plain\n";
print "\n";
print "This is users list.\n";
f = open("data/user.data")
lines = f.readlines()
f.close()

header = lines[0].split(',')
for item in header:
	print "[", item.rstrip(), "]",
print 
for line in lines[1:]:
	data = line.split(',')
	for item in data:
		print item.rstrip(), "|",
	print
print
