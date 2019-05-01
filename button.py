from tkinter import *
import tkinter.messagebox as mb

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

def helloCallBack():
	mb.showinfo( "MB_Title_Hello Python", "MB_MSG_Hello World")

B = Button(app_window, text ="button_text_hello", command = helloCallBack)
B.pack()

app_window.mainloop()
