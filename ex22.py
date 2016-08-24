print "# This char it work for comment"
print "The word print it work for printer in monitor the sinxtax is: print 'text'"
print '\tOr sixtax is: print "text"'
print """
	Other form the print is: print 'text', number, number or operacion,....,n
	the numers can to be constants.
"""
print """
	The aritmeth operacions are:
		add = + example 1+1
			print 1+1 this is correct
			print "Result", 1+1 is correct
		substract = - example 10-1
			print 10-1
			print "text", 10-1
		multiply = * example 1*4
			print 1*4
			print "text",1*4
		div = / example 10/2
			print 10/2
			print "text", 10/2

	The comparation are:
		>, >=, <,<= if result is true return TRUE else retunr False
		
"""
print """
	The asignations of variables, example:
		var1 = 10
		var2 = var1-10
		var3 = var1-var2
		they can all aritmethic operations
"""

print """
	Other form of print  is print "text",variable,"text
"""

print """
	Other form of print is print "text %s" % name where %s its the place where go the result of variable
	if are more variables it is the struct:
	print "Text %s %s %s" % (var1,var2,var3)
"""

print """
	formatter is utiliced for acomoding the vars
	example formatter="%r %r
	
	print formatter % (var1,var2)
"""

formatter = "hi variable 1 %r, hi variable2 %r"

print formatter %(1,2)
print formatter %("Hello","Hi")

print"""
	raw_input is for to put some dat 
	example var1 = raw_input()
"""

print"""
	Other form = var = raw_input("text")
"""

print"""
	from sys import argv if for import variabls of the to run the program
	example: script.py var1, var2
	
		from sys import argv
		
		script, var1, var2

		code
		.
		.
		.
		asignement to variabls var1 and var2
"""

print"""
	file
	aisgnement variable to file
		file = open(filename) #open file and asignement to var file
		read de file is file.read()
		close teh fila is file.close()
"""
print"""
	open file mode write is variable = open(filename,'w')
	empty file is variable.trucate()
	writ in file id variable.write("varabls, or text")
"""

print"""
	len obtains the size of file example:
	x = len(varFile)
"""

print"""
	functions sintax
	def name_function(*args): # *args = n varaibles

	function complet

	function example(x,y):
		z = x-y
		return z

	result = example(1,2)
	
	result = -1
"""
