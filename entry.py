from tkinter import *

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

label1 = Label(app_window, text="User Name")
label1.pack( side = LEFT)
entry1 = Entry(app_window, bd =5)   # bd -- border size 5 pixels
entry1.pack(side = RIGHT)

app_window.mainloop()
