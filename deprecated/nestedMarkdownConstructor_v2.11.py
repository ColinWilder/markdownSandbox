# nestedMarkdownConstructor

# Version history:
	# V1 was the basic alpha.
	# V2.11 rewrites the code for simpler flow of control and changes the grammar of the #include statement. 
# Ideas for changes are in separate notes doc.

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
			
			# check whether line has an #include statement
			doesInclude = line.find("#include")
			
			# no #include statement
			if doesInclude == -1:
				contentsOfArgumentFile += line; #print("contentsOfArgumentFileR: " + contentsOfArgumentFile)
			
			# has #include statement
			else:
				
				# here you should check whether line begins with #include and ends with .md. If not, error. 
				
				# locate start of filename
				startOfIncludeStatement = doesInclude + 9
				# locate end of filename (incl. .md)
				endOfIncludeStatement = line.find(".md")+3
				# isolate and rip complete included filename
				nameOfIncludedMDFile = line[startOfIncludeStatement:endOfIncludeStatement]
				#print(nameOfIncludedMDFile) # note that as coded this will also print the "#include" part.
				
				# recur to extract contents of nested file
				#print("...doing recursive dive")
				argumentForRecursiveDive = nameOfIncludedMDFile #; print(argumentForRecursiveDive)
				returnedResultOfRecursiveDive = nest(argumentForRecursiveDive) # recur using that tempstring as argument
				#print("returnedResultOfRecursiveDive: " + str(returnedResultOfRecursiveDive))
				#print("returned from dive with: " + returnedResultOfRecursiveDive)
				contentsOfArgumentFile += returnedResultOfRecursiveDive # when it pops back out of its recursive punge, it has to add ts return to contentsOfArgumentFile
	
		f.close()
		return contentsOfArgumentFile

fullOutput = nest("Chapter2_Ideas.md")
print(fullOutput)
