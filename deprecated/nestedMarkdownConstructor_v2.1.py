# nestedMarkdownConstructor_v2.1.py
# Ideas for changes are in separate notes doc.
# Version history: V1 was the basic alpha. V2.x is going to be me trying to rewrite for simplicity; begun agun 3/25/21.

def nest(mdFile):
	
	# make empty output string where the entire nested contents will ultimately be put
	contentsOfArgumentFile = ""
	
	# open file
	with open(mdFile,'r+') as f:
		
		# read all the lines in the file into a variable called lines
		lines = f.readlines(); #print("reading lines of argument file")
		
		# loop through the lines one by one
		for i in range(0,len(lines)):
			
			# make a more local string variable in this loop to contain the contents of the line being presently examined
			line=lines[i]; #print("line " + str(i) + " in argument file: " + line[:-1])
			#print(line[:-1])
			#print("length of line: " + str(len(line)))
			
			# case: line is too short to contain an #include statement
			if len(line) < 13:
				#print("... line*" + line + "* is too short to have statement")
				
				# add content of line to output string
				contentsOfArgumentFile += line; #print("contentsOfArgumentFileQ: " + contentsOfArgumentFile) # record its content
				continue # continue the for loop

			# check whether line has an #include statement
			else:
				doesInclude = line.find("#include")
				
				# case: no include statement
				if doesInclude == -1:
					contentsOfArgumentFile += line; #print("contentsOfArgumentFileR: " + contentsOfArgumentFile)
				
				# case: has an #include statement
				else:
					
					# add content of string *before* #include statement to output string # this can be deleted or changed to return error
					contentsOfArgumentFile += line[0:doesInclude]; #print("contentsOfArgumentFileR: " + contentsOfArgumentFile) # record content of inital part
					startOfIncludeStatement = doesInclude + 9
					# locate the .md filename after this
					endOfIncludeStatement = line.find(".md")+3 # first look for the marker ".md" and working backward
					nameOfIncludedMDFile = line[startOfIncludeStatement:endOfIncludeStatement] # copy the file name to a temp string
					# print(nameOfIncludedMDFile) # note that as coded this will also print the "#include" part.
					#print("...doing recursive dive")
					argumentForRecursiveDive = nameOfIncludedMDFile #; print(argumentForRecursiveDive)
					returnedResultOfRecursiveDive = nest(argumentForRecursiveDive) # recur using that tempstring as argument
					#print("returnedResultOfRecursiveDive: " + str(returnedResultOfRecursiveDive))
					#print("returned from dive with: " + returnedResultOfRecursiveDive)
					contentsOfArgumentFile += returnedResultOfRecursiveDive # when it pops back out of its recursive punge, it has to add ts return to contentsOfArgumentFile
	
		f.close()
		return contentsOfArgumentFile

print(nest("Chapter2_Ideas.md"))
