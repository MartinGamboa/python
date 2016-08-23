from sys import argv

script, filename = argv #charge file in arguments

txt = open(filename) #open file assigned to txt

print "Here's your file %r:" %filename #it see name file
print txt.read() #printer the variable in monitor

print "Type the filename again:"
file_again= raw_input("> ") #ask name file

txt_again = open(file_again) #asigned value to the txt again

print txt_again.read() #printer value asigned

txt.close()
txt_again.close();
