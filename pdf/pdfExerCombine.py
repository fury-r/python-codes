import PyPDF2
import sys
a=sys.argv[1:]
def combine(pdflist):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdflist:
        print(pdf)
        merger.append(pdf)
    merger.write("doc/super.pdf")
print(a)
combine(a)