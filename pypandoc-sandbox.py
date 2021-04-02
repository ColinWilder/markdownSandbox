# pypandox sandbox
# https://pypi.org/project/pypandoc/

import pypandoc

# With an input file: it will infer the input format from the filename
output1 = pypandoc.convert_file('Ch1.md', 'rst')
# print(output1)

# ...but you can overwrite the format via the `format` argument:
output2 = pypandoc.convert_file('simpleBookEx.txt', 'rst', format='md')
# print(output2)

# alternatively you could just pass some string. In this case you need to
# define the input format:
output3 = pypandoc.convert_text('Hello world!', 'rst', format='md')
# print(output3)

# It's also possible to directly let pandoc write the output to a file. This is the only way to convert to some output formats (e.g. odt, docx, epub, epub3, pdf). In that case convert_*() will return an empty string.
output4 = pypandoc.convert_file('Ch1.md', 'docx', outputfile="Ch1.docx")
assert output4 == "" # I think this assert statement is sort of an error-checker to confirm that the conversion process went right. 
