x = "There are %d types of people." %10 #it shows number 10 in %d
bynary = "bynary" #assign variable to bynary
do_not = "don't" #assign variable to do_not
y = "Those who know %s and those who %s."% (bynary, do_not)#it shows variables in %s in order

print x
print y

print "I said: %r." % x #it shows the variable x in %r
print "I also said: '%s'." % y #it shows y , y container to variable bynary and do_not

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #assign direct variable hilarious in print

w = "This is the left side of...."
e = "a string width a right side."

print w + e #concat variable w and e directly
