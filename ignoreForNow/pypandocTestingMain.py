import pypandoc
output = pypandoc.convert_file('testContent1.txt', 'rst', format='md')
print(output)

# did this actually produce a file? I don't think so...