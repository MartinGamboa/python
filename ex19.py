def cheese_and_crackers(cheese_count, boxes_of_crackers): #function inte the two variables
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of creakers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)# call function with two numbers

print "Or, we can use variables from our scrpt:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)


def suma(num1,num2):
	result = num1+num2
	print "The result of the sum of the %d + %d  is: %d" % (num1,num2,result)


suma(1,3)

num1 = 1
num2 = 5

suma(num1,num2)

suma(num1+num2,1)

suma(11,12)

suma(1*2,4*4)

suma(num2,45)

suma(num1*num2,-99)

suma(-99,-99)

suma(num1,num2-5)

suma(10,-10+7) 
