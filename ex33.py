i = 0
numbers = []

j = 110

while i < j:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 5
	print "NUmbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
