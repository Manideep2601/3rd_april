from tkinter import *

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

text = Text(app_window)
text.insert(INSERT, "Python is \n")
text.insert(INSERT, "easy \n")
text.insert(END, "to learn....")
text.pack()

app_window.mainloop()
