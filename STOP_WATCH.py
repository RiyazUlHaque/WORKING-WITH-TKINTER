# PROGRAM OF STOP-WATCH
#VERSION PYTHON 2.7
from Tkinter import *
import ttk
import Tkinter
 
counter=0

def count_lable(lable):
	counter=0
	def count():
		global counter
		
		counter=counter+1
		label.config(text=str(counter))
		label.after(100,count)
	count()
	
root=Tk()
root.title("TIME COUNTING")
label=Label(root, fg = "darkgreen")
label.pack()
count_lable(label)
button=Button(root,text="STOP" , width=25, command=root.destroy)
button.pack()
root.mainloop()

#PRINT THE VALUE OF COUNTER
print "YOU HAVE STOPPED AT ",counter
	