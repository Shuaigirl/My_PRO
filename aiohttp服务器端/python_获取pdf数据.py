# _*_coding:utf-8_*_
# @Time:2022/4/27 11:12
# @Author:Young
# @File:python_获取pdf数据

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("demo/test.pdf", "rb"))

def delete_pdf(index):
 pages = input1.getNumPages()

 for i in range(pages):
  if i+1 in index:
   continue
  output.addPage(input1.getPage(i))

 outputStream = open("PyPDF2-output.txt", "wb")
 output.write(outputStream)

# delete_pdf([2,3,4])