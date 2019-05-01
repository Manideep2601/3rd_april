from tkinter import *

app_window = Tk()

# defining size of window 
app_window.geometry("600x600") 
  
# setting up the title of window 
app_window.title("App Title") 

B1 = Button(app_window, text ="FLAT", relief=FLAT )
B2 = Button(app_window, text ="RAISED", relief=RAISED )
B3 = Button(app_window, text ="SUNKEN", relief=SUNKEN )
B4 = Button(app_window, text ="GROOVE", relief=GROOVE )
B5 = Button(app_window, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()

app_window.mainloop()
