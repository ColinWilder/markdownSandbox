def nest(mdFile):
	contentsOfArgumentFile = ""
	with open(mdFile,'r+') as f:
		lines = f.readlines(); #print("reading lines of argument file")
		for i in range(0,len(lines)): # each i corresponds to a line in mdFile
			line=lines[i]; #print("line " + str(i) + " in argument file: " + line[:-1])
			#print(line[:-1])
			#print("length of line: " + str(len(line)))
			if len(line) < 13: # line is too short to contain an #include flag
				print("...line too short to have statement")
				contentsOfArgumentFile += line; #print("contentsOfArgumentFileQ: " + contentsOfArgumentFile) # record its content
				continue # continue the for loop
			else:
				doesInclude = line.find("#include")
				if doesInclude == -1:
					contentsOfArgumentFile += line; #print("contentsOfArgumentFileR: " + contentsOfArgumentFile)
				else:
					contentsOfArgumentFile += line[0:doesInclude]; #print("contentsOfArgumentFileR: " + contentsOfArgumentFile) # record content of inital part
					startOfIncludeStatement = doesInclude + 9
					# locate the .md filename after this
					endOfIncludeStatement = line.find(".md")+3 # first look for the marker ".md" and working backward
					nameOfIncludedMDFile = line[startOfIncludeStatement:endOfIncludeStatement] # copy the file name to a temp string
					# print(nameOfIncludedMDFile) # note that as coded this will also print the "#include" part.
					#print("...doing recursive dive")
					argumentForRecursiveDive = nameOfIncludedMDFile # + ".md"; print(argumentForRecursiveDive)
					returnedResultOfRecursiveDive = nest(argumentForRecursiveDive) # recur using that tempstring as argument
					#print("returnedResultOfRecursiveDive: " + str(returnedResultOfRecursiveDive))
					#print("returned from dive with: " + returnedResultOfRecursiveDive)
					contentsOfArgumentFile += returnedResultOfRecursiveDive # when it pops back out of its recursive punge, it has to add ts return to contentsOfArgumentFile
	
		f.close()
		return contentsOfArgumentFile

print(nest("Chapter2_Ideas.md"))
