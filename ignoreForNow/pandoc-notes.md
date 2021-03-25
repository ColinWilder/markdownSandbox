# Lessons

Sustainable Authorship in Plain Text using Pandoc and Markdown | PH. https://programminghistorian.org/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown

Building books with Markdown using pandoc | Programmers-Developers | Medium. https://medium.com/programmers-developers/building-books-with-markdown-using-pandoc-f0d19df7b2ca

https://pandoc.org/epub.html


## Commands and initial notes
pandoc PH_sustainableAuth_lesson_source.md -o PH_sustainableAuth_lesson_target.pdf
pandoc PH_sustainableAuth_lesson_source.md -o PH_sustainableAuth_lesson_target.html
pandoc PH_sustainableAuth_lesson_source.md -o PH_sustainableAuth_lesson_target.docx
pandoc -o buildingBooks_lesson_source.docx buildingBooks_lesson_source.md  <!--This shows that you can name the input file anywhere; here is comes last.-->

-s or -standalone <!-- This flag makes the output a piece of standalone HTML, with header etc. tags. This flag seems to make no difference with ePubs, but makes HTML style rendering much better. -->

-o <!-- This flag designates the name of the output file. If omitted, output goes to stout. -->

# MS Word docs (.docx)
## From .md to .docx
pandoc -o myBookOutput3.docx Ch1.md Ch2.md
## From .docx to .md
pandoc C0-endMatter-index.docx -o C0-endMatter-index.md <!--This worked fine, producing a .md file. The only loss was that the MS Word footer did not come through.-->
## Varia
For open/libre office, use .odt instead. 


# Metadata file
See the metadata file in the project folder. 
pandoc -o myBookContent.pdf myBookOutput.md metadata.txt

# Stylesheet
See .epub stylesheet file in project folder. 

# Table of contents
--toc
pandoc --toc -o myBookOutput.epub metadata.txt myBookContent.md
<!-- It is necessary to place the flag at the beginning. Putting it at the end screwed things up and made the metadata appear after the last chapter. -->

## Working with .txt source files
This can be a .txt. See toy example at https://pandoc.org/epub.html. 
pandoc simpleBookEx.txt -o simpleBookExOutput.epub
Seems to assume that the first % indicates the title. Autogenerates a title page basedon inital % things. Very lightweight but ambiguous. Given that the markdown and metadata versions of stuff seem to offere a lot more power...


# Try to build a book from several .md files all in the same folder

The next step would be to do this all in one master folder. My ghost tells me that will work just fine. 

pandoc -o myBook2Output.epub metadata.txt Ch1.md Ch2.md <!-- This worked. -->


# pypandoc

import pypandoc
output = pypandoc.convert_file('testContent1.txt', 'rst', format='md')

# Big reset

I've uninstalled Python 2, Python 3, Pandoc, and Node. 
