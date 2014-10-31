#########################################
#
#         85pt - Add a cancel button
#
#########################################


# Add a cancel button with a red background
# When the cancel button is pressed, change the color from red to blue
# and then back to red when pressed again

from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent  ### (7) remember my parent, the root
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		#Added more information regarding button
		self.myContainer2 = Frame(parent)
		self.myContainer2.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)	
		self.button1.bind("<Button-1>", self.button1Click) ### (1)
		#Added button information such as text and background color
                self.button2 = Button(self.myContainer2)
		self.button2.configure(text="Cancel", background= "red")
		self.button2.pack(side=LEFT)	
		self.button2.bind("<Button-1>", self.button2Click)
		
	def button1Click(self, event):    ### (3)
		if self.button1["background"] == "green": ### (4)
		      self.button1["background"] = "yellow"
		else:
		      self.button1["background"] = "green"
	# Created a new function for button2		
	def button2Click(self, event):
	        if self.button2["background"] == "red": ### (4)
		      self.button2["background"] = "blue"
	        else:
		      self.button2["background"] = "red"
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()