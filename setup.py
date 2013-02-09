#Sets up the dotfiles for the current user
#Create a symbolic link for everything in the dot file directory
#To the user's home folder

#Imports
import os
import subprocess

#Creates a symbolic link for the passed in data
#sourceLocation - origional source file 
#targetLocation - location where the source file will reference

def createSymbolicLink (sourceLocation, targetLocation):
	try:
		subprocess.check_output("ln -s " + sourceLocation + " " + targetLocation)
	except subprocess.CalledProcess, e:
		print "Error: " + e + " for symlink of: " + sourceLocation + " and " + "targetLocation" 

#Return an array of files in the dot files directory
#Exclude any unnecessary files
def getDotFiles ():
	
	#List of excluded files
	excludedFilesList = [".DS_Store", ".git", ".gitignore", ".sdirs", ".netrwhist"]
	returnFileList = []
	
	#Get all files in the dotfiles directory
	allDotFilesList = subprocess.Popen("find " + dotFilesDirectory + " -name \".*\" -maxdepth 2",stdout=subprocess.PIPE, shell=True) 
	
	#Loop through all items in the allDotFilesList and return a list of files that
	#are not in the blacklist
	while True:
		isExcluded = False
		#Split the full path, only get the filename
		currentFile = allDotFilesList.stdout.readline().rstrip().rsplit('/',1)[-1]
		#Sanity check - verify the currentFile is valid
		if not currentFile:
			break
		else:
			#Check the currentFile against all items in the excludedFilesList
			for excludedFile in excludedFilesList:
				#currentFile is excluded, mark currentFile as excluded
				if currentFile == excludedFile:
					isExcluded = True
			
			#File should not be excluded, add to returnFileList
			if isExcluded != True:
				returnFileList.append(currentFile)
			
	#Return the filtered list
	return returnFileList

if __name__ == "__main__": 
	
	#Setup
	#Define the dotFiles path
	dotFilesDirectory = os.getcwd()	+ "/"

	#Current User 
	currentUser = subprocess.check_output("stat -f%Su /dev/console", shell=True).rstrip()
	#Define the current user's home dir
	currentUserHomeDirectory = "/Users/" + currentUser + "/"

	#Get a list of files in the dotfiles directory and create a symbolic link for the file
	for currentFile in getDotFiles():
		createSymbolicLink(dotFilesDirectory + currentFile, currentUserHomeDirectory + currentFile)
	

