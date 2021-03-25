# recursive function

# This basically works now. Fri. 3/19/21, 11:04 PM.
# Change the grammar so that an #include statement has to begin a line, will not be processed if it comes after position 0, and anything after the .md in the #include statement's argument will not be processed.
# use the HTML wrapper utility from PH, with a browser tab opening up, to view both source .md file(s) and build result file.
# The code should ignore empty lines it encounters in source .md file(s). 

def nestedMarkdownConstructor(mdFile):
	print("starting")
	f = open(mdFile,'r'); print("opened file")
	contentsOfArgumentFile=""; print("contentsOfArgumentFile: " + contentsOfArgumentFile)
	with open(mdFile,'r+') as f:
		lines = f.readlines(); print("reading lines of argument file")
		for i in range(0,len(lines)): # each i corresponds to a line in mdFile
			line=lines[i]; print("line " + str(i) + " in argument file: " + line[:-1])
			print("length of line: " + str(len(line)))
			if len(line) < 13: # line is too short to contain an #include flag
				print("line too short to have #include statement")
				contentsOfArgumentFile += line; print("contentsOfArgumentFileQ: " + contentsOfArgumentFile) # record its content
				continue # continue the for loop
			else:
				doesInclude = line.find("#include")
				if doesInclude == -1:
					contentsOfArgumentFile += line; print("contentsOfArgumentFileR: " + contentsOfArgumentFile)
				else:
					contentsOfArgumentFile += line[0:doesInclude]; print("contentsOfArgumentFileR: " + contentsOfArgumentFile) # record content of inital part
					startOfIncludeStatement = doesInclude + 9
					# locate the .md filename after this
					endOfIncludeStatement = line.find(".md")+3 # first look for the marker ".md" and working backward
					nameOfIncludedMDFile = line[startOfIncludeStatement:endOfIncludeStatement] # copy the file name to a temp string
					print(nameOfIncludedMDFile)
					print("doing recursive dive")
					returnedResultOfRecursiveDive = nestedMarkdownConstructor(nameOfIncludedMDFile) # recur using that tempstring as argument
					print("returned from dive with: " + returnedResultOfRecursiveDive)
					contentsOfArgumentFile += returnedResultOfRecursiveDive # when it pops back out of its recursive punge, it has to add ts return to contentsOfArgumentFile
	f.close() # close mdFile
	return contentsOfArgumentFile

print(nestedMarkdownConstructor("Chapter2_Ideas"))
