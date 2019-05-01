from tkinter import *

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

topframe = Frame(app_window)
topframe.pack(side=TOP)

leftframe = Frame(app_window)
leftframe.pack(side=LEFT)

rightframe = Frame(app_window)
rightframe.pack(side=RIGHT)

bottomframe = Frame(app_window)
bottomframe.pack(side=BOTTOM)


redbutton = Button(topframe, text="Red", fg="red")
redbutton.pack()


greenbutton = Button(leftframe, text="Brown", fg="brown")
greenbutton.pack()

bluebutton = Button(rightframe, text="Blue", fg="blue")
bluebutton.pack()

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack()


app_window.mainloop()
