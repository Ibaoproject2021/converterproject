'''
Image Converter 
Created By: Ivan Brix A Olaguir
Free To Use
Open Source
'''

# Imports
from tkinter import*
from PIL import Image, ImageTk
import webbrowser
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os

# Screen
root = Tk()
root.title("Ibao Image Converter")
root.geometry("400x210")
root.configure(bg="#5d5e5c")
root.resizable(0,0)
root.iconbitmap("C:\\Users\\Nap\\Desktop\\Python project\\icon\\iconconverter.ico")

# Label Screen
label = Label(root, width=50, height=1, bg='#59ff00', fg="black", relief='sunken', bd=2, justify="left")
label.pack(pady=5, anchor=CENTER)

my_label = Label(root, text="Image Converter", fg='cyan', bg='#5d5e5c', font=("BOLD"))
my_label.pack(pady=10)

label_1 = Label(root, width=50, height=1, bg='#59ff00', fg="black", relief='sunken',)
label_1.pack(pady=1, anchor=CENTER)

convert_label = Label(root, text="Convert To", fg='red', bg='#5d5e5c', font=("BOLD", 16))
convert_label.pack(pady=5, anchor=CENTER)


# Functions
def source_code():
	webbrowser.open("https://github.com/Ibaoproject2021/ibaoproject/blob/main/converter.py")

def Open_PNG():
    global img
    PNG_file_path = filedialog.askopenfilename(title="Open PNG", filetype=(("PNG File", "*.png"), ("All Files", "*.*")))
    img = Image.open(PNG_file_path).convert('RGB')
    label.config(text=f'{PNG_file_path}')

def	Open_JPG():
	global img
	JPG_file_path = filedialog.askopenfilename(title="Open JPG", filetypes=(("JPG File", "*.jpg"), ("All Files", "*.*")))
	img = Image.open(JPG_file_path)
	label.config(text=f'{JPG_file_path}')

def JPG():
    global img
    try:
    	JPG_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    	img.save(JPG_file_path)
    	label_1.config(text=f'{img}')
    except:
    	messagebox.showerror("Ibao Image Converter", "Error: No File selected")

def PNG():
	global img
	try:
		PNG_export = filedialog.asksaveasfilename(defaultextension='.png', title="Save PNG File", filetypes=(("PNG File", "*.png"), ("All Files", "*.*")))
		img.save(PNG_export)
		rgb = img.convert('RGB')
		label_1.config(text=f'{img}')
	except:
		messagebox.showerror("Ibao Image Converter", "Error: No File selected")

def ICON():
	global img
	try:
		ICON_export = filedialog.asksaveasfilename(defaultextension='.ico', title="Save Icon File", filetypes=(("Icon File", "*.ico"), ("All Files", "*.*")))
		img.save(ICON_export)
		label_1.config(text=f'{img}')
	except:
		messagebox.showerror("Ibao Imgae Converter", "Error: No File selected")


# Frame 
frame = Frame(root, bg="white")
frame.pack(side=BOTTOM, pady=10, padx=10)

convert_Button = Button(frame, text="JPG", width=10, height=0, bd=2, command=JPG, fg="white", bg="skyblue", font=("Bold"))
convert_Button.grid(row=1, column=1, sticky=W, ipadx=5)

convert_Button = Button(frame, text="ICON", width=10, height=0, bd=2, command=ICON, fg="white", bg="skyblue", font=("Bold"))
convert_Button.grid(row=1, column=2, sticky=W, ipadx=5)

convert_Button = Button(frame, text="PNG", width=10, height=0, bd=2, command=PNG, fg="white", bg="skyblue", font=("Bold"))
convert_Button.grid(row=1, column=3, sticky=W, ipadx=5)

def About():
	root = Tk()
	root.title("Ibao Image Converter")
	root.geometry("300x110")
	root.configure(bg="#000000")
	root.resizable(0,0)
	root.iconbitmap("C:\\Users\\Nap\\Desktop\\Python project\\icon\\iconconverter.ico")
	root.overrideredirect(False)
	Label(root, text="Created By: Ivan Brix A. Olaguir", font=("Helvetica", 15), fg="#fc0303").pack(pady=10)
	Button(root, text="Okay", width=10, height=0, bd=3, bg="#ff00ee", fg="white", command=lambda: root.destroy()).pack(pady=15)

	root.mainloop()

# Menu Bar 
menuBar = Menu(root)
root.config(menu=menuBar)

# File Menu
file_menu = Menu(menuBar, tearoff=False)
file_menu.add_separator()
file_menu.add_command(label="Open PNG Image", command=Open_PNG)
file_menu.add_command(label="Open JPG Image", command=Open_JPG)
file_menu.add_command(label="Exit", command=lambda: root.destroy())
menuBar.add_cascade(labe="File", menu=file_menu)

# Help Menu
help_menu = Menu(menuBar, tearoff=False)
help_menu.add_separator()
help_menu.add_command(label="Source Code", command=source_code)
help_menu.add_command(label="About", command=About)
menuBar.add_cascade(labe="Help", menu=help_menu)

# Mainloop
root.mainloop()


# Thank you for using my program