from tkinter import *

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

var = StringVar()
label = Label( app_window, textvariable=var, relief=RAISED )

var.set("Hello World !!")
label.pack()

app_window.mainloop()
