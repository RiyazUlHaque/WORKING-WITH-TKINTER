#HOW TO MAKE BUTTON IN A WINDOW

from tkinter import *
 
root=Tk()
def end(e):
	root.destroy()     #THIS WILL CLOSE THE WINDOW
	

#BUTTON CODE
button1=Button(root,text="BUTTON-1",bg="lightgreen")
button1.pack()

#BUTTON CODE _ ONCE AFTER CLICKING ON THE BUTTON , WINDOW WILL GET CLOSED 
button2=Button(root,text="EXIT",bg="lightblue")
button2.bind('<Button-1>',end)
button2.pack()

root.mainloop()