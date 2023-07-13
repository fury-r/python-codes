import PyPDF2



reader=PyPDF2.PdfFileReader(open("doc/super.pdf",'rb'))
output = PyPDF2.PdfFileWriter()
watermark=PyPDF2.PdfFileReader(open("doc/11.3 wtr.pdf",'rb'))
for i in range(reader.numPages):
    pos=reader.getPage(i)
    pos.mergePage(watermark.getPage(0))
    output.addPage(pos)
output.write(open("watermark.pdf","wb"))
print("Done!")