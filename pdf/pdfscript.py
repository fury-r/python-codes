
import PyPDF2

render=PyPDF2.PdfFileReader( open("./doc/11.2 twopage.pdf", "rb")) #read binary
writer=PyPDF2.PdfFileWriter()
page=render.getPage(0)
print(render.numPages)
r=page.extractText()
print(r)
print(render.getPage(0))
a=page.rotateClockwise(90)
writer.addPage(a)
writer.addBlankPage()
writer.write(open("./doc/tilt.pdf","wb" ))
