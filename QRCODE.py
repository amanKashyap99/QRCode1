import qrcode as qr
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
class QR():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title(" QRCode Generator ")
        self.mainframe = tk.Frame(self.root, background="#ff9999")
        self.mainframe.pack(fill='both', expand=True)
        self.txt1 = ttk.Label(self.mainframe, text="Enter The Data : ", font=("comic sans ms", 14, "bold"),background="#ff9999")
        self.txt1.place(x=30, y=30, height=50, width=200)
        self.qdata = ttk.Entry(self.mainframe)
        self.qdata.place(x=210,y=40,height = 25 ,width=170  )
        self.wbtn = ttk.Button(self.mainframe, text=" Get QRCode ",command = self.genQR)
        self.wbtn.place(x=125, y=110, height=30, width=150)
        self.root.mainloop()
    def genQR(self):
        self.qrcode = qr.QRCode(version=1,box_size=5,border=1)
        self.qrcode.add_data(self.qdata.get())
        self.qrcode = self.qrcode.make_image(fill_color= "#ff1919",back_color="#f0b2f0")
        self.qrcode.save("new.png")

        self.photo = Image.open("new.png")
        self.rphoto = self.photo.resize((120,120),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.rphoto)

        self.txt2 = ttk.Label(self.mainframe, image=self.photo,background="#ff9999")
        self.txt2.place(x=140, y=170,)
        self.txt2 = ttk.Label(self.mainframe, text="Your QRCode is Ready ^_^  ", font=("comic sans ms", 14, "bold"),background="#ff9999")
        self.txt2.place(x=75, y=300, height=50, width=280)
QR()