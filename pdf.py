import sys, fitz
import os 
from tkinter import *
from tkinter import filedialog

pic = []
pdf = ''

def removeAll():
    global pic
    pic.clear()
    txt4.configure(text="")

def removeLast():
    global pic
    if len(pic) != 0:
        pic.pop(len(pic)-1)
        if len(pic) != 0:
            for x in reversed(range(len(pic[0]))):
                if pic[0][x] == '/' or pic[0][x] == '\\':
                    n = pic[0][x+1:]
                    break
            txt4.configure(text=n + '(+'+str(len(pic)-1)+')')
        else:
            txt4.configure(text="")

def convert():
    doc = fitz.open()
    for i, f in enumerate(pic):
        image = fitz.open(f)
        size = image[0].rect
        pdfb = image.convertToPDF()
        image.close()
        imgpdf = fitz.open("pdf", pdfb)
        page = doc.newPage(width = size.width, height = size.height)
        page.showPDFpage(size, imgpdf, 0)
    doc.save(pdf)

def upload(event=None):
    global pic
    pic.append(filedialog.askopenfilename())
    for x in reversed(range(len(pic[0]))):
        if pic[0][x] == '/' or pic[0][x] == '\\':
            n = pic[0][x+1:]
            break
    txt4.configure(text=n + '(+'+str(len(pic)-1)+')')

def name(event=None):
    global pdf
    i=0
    pdf = ent.get() + '.pdf'
    if len(pdf) <= 4:
        txt3.configure(text='No name entered!', fg='red')
    elif len(pic) == 0:
        txt3.configure(text='No file selected', fg='red')
    else:
        for a in pic:
            if a[-3:] == 'png' or a[-3:] == 'jpg' or a[-4:] == 'jpeg':
                i+=1
                if len(pic) == i:
                    txt3.configure(text='Created!', fg='green')
                    convert()
            else:
                txt3.configure(text='Not image(s)', fg='red')
                break


top = Tk()
top.title("PDF Converter")
top.geometry('400x250')

txt = Label(top, text = "Select images:") 
txt.grid()

btn = Button(top, text = "  +  ", command=upload)
btn.grid(column=2, row=0)

txt2 = Label(top, text = "Enter a name for PDF:   ")
txt2.grid()

ent = Entry(top, width=10)
ent.grid(column=1, row=1)

btn2 = Button(top, text = "Okay", command=name)
btn2.grid(column=2, row=1)

txt3 = Label(top)
txt3.grid(column=1)

txt4 = Label(top)
txt4.grid(column=1, row=0)

btn3 = Button(top, text = "remove last", command=removeLast)
btn3.grid(column=1, row=5)

btn4 = Button(top, text = "remove all", command=removeAll)
btn4.grid(column=2, row=5)

top.mainloop()
