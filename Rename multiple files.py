import os 
from tkinter import *
import tkinter as tk
def off():
    window.destroy()    
def image_rename():
    folder = e1.get()
    imagename = e2.get()  
    for count,filename in enumerate(os.listdir(folder)):
        dst = f"{imagename}-{str(count)}.jpg"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"
        os.rename(src,dst)       
window = tk.Tk()
window.geometry("450x250")
window.config(bg="#BB78FF")
window.resizable(width=False,height=False)
window.title('Image Rename')

l1 = tk.Label(window,text="Image Rename",font=("Arial", 20),fg="black",bg="#D2FFFF")
l2 = tk.Label(window,font=("Arial",12),text="Enter the Image Folder Url to Rename the Image",fg="black",bg="#D2FFFF")

l_d=tk.Label(window,text="Enter Folder Url: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#D2FFFF")
l_m=tk.Label(window,text="Images Name:",font=('Arial',12,"bold"),fg="darkgreen",bg="#D2FFFF")


e1=tk.Entry(window,width=20)
e2=tk.Entry(window,width=20)


b1=tk.Button(window,text="Change",font=("Arial",13),command=image_rename)

b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=off)
l3 = tk.Label(window,text="Developed By Aleem Raza",font=("Arial", 20),fg="black",bg="#D2FFFF")
l1.place(x=150,y=5)
l2.place(x=70,y=40)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
e1.place(x=250,y=70)
e2.place(x=250,y=95)
b1.place(x=150,y=130)
b2.place(x=250,y=130)
l3.place(x=80,y=200)
window.mainloop()