import sys
import os
import re

def sortFunction(ipFile,opFile):

	# Define 3 arrays: Integer, String, Result
	intArray, alphaArray, resultArray  = [],[],[]
	try:
		# Reading contents of the file
		fileReader = open (ipFile,'r')
		fileContent = fileReader.read ()
	except:
		print ("There was an error while running the program.Please see the details below \n")
		errType, errValue, errTraceback = sys.exc_info()
		print ("ErrorType:"+str(errType)+" Error on line:"+str(errTraceback.tb_lineno))
		print ("\nPlease try again ! \nExsiting the program\n")	
		sys.exit()

	# Using regular expression allow only space, number and chraacters (a-z A-Z).
	fileContent = re.sub("[^ 0-9a-zA-Z]","",fileContent)

	# This for loop will spilt digits and alphabets and store in array intArray and alphaArray respectively.
	for i in fileContent.split():
		if i.isdigit():
			intArray.append(int(i))
		else:
			alphaArray.append(str(i))

    # Using the sort (), sort both the arrays.
    # The sort () by default sorts in ascending order. 
    # Since we will be using pop which follows FILO principle we are converting the sort in decending order |reverse = true| 
	alphaArray.sort(reverse=True,key=lambda s:s.lower())
	intArray.sort(reverse=True)


	# This for loop will spilt the alphabets and digits array and append it in result array  
	for i in fileContent.split():
	    if i.isdigit():
	        resultArray.append(intArray.pop()) 
	    else:
	        resultArray.append(alphaArray.pop())

	# Write the result in the output file       
	fileWriter = (open(opFile,'w'))
	fileWriter.write(" ".join(map(str,(resultArray))))

	# Close fileReader and fileWriter	
	fileReader.close()
	fileWriter.close()

	print ("Completed "+sys.argv[0]+" program")
	outputFilePath = os.path.abspath(sys.argv[2])
	print ("Output can be found here: "+outputFilePath)


def main ():
	print ("\nStarted "+sys.argv[0]+" program")
	print ("...........................\n")
	print ("...........................\n")

	# Read the input and output file from command line.
	try:
		inputFile = str(sys.argv[1])
		outputFile = str(sys.argv[2])
	
	# If the arguments are not found catch an exception and exit the program.
	except:
		print ("There was an error while running the program.Please see the details below \n")
		print ("Usage: fileName.py inputFile.txt outputFile.txt")	
		errType, errValue, errTraceback = sys.exc_info()
		print ("ErrorType:"+str(errType)+" Error on line:"+str(errTraceback.tb_lineno))
		print ("\nPlease try again ! \nExsiting the program\n")	
		sys.exit()

	sortFunction(inputFile,outputFile)	

main ()

"""
For catching an exception,to get the type, file, and line number.
errType, errValue, errTraceback = sys.exc_info()
http://stackoverflow.com/questions/1278705/python-when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number

To convert item in list to string
" ".join(map(str,(resultArray)))
http://www.decalage.info/en/python/print_list
"""