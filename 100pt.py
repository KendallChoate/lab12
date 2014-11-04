#########################################
#
#         100pt - Working with Canvas
#
#########################################


# Add a button called "Right"
# Make it so that when you press the button, the oval moves to the left or right

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=480,height=320, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")
direction = 1
class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		#Added more button information
		self.myContainer2 = Frame(parent)
		self.myContainer2.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.pack(side=LEFT)
		
	        # Add a second button!
		# Added second button called "Right"	
		
		self.button2 = Button(self.myContainer2)
		self.button2.configure(text="Right", background= "cyan")
		self.button2.pack(side=LEFT)		
						
		self.button1.bind("<Button-1>", self.button1Click) 
		drawpad.pack(side=BOTTOM)
		# Added button2 information
		self.button2.bind("<Button-1>", self.button2Click) 
		drawpad.pack(side=BOTTOM)

		
	def button1Click(self, event):   
		# Move to the left
		global oval
		global drawpad
		drawpad.move(oval, -10, 0)
		
	# Add the event handler for the second button!	
	
	def button2Click(self, event):   
		# Move to the right
		global oval
		global drawpad
	        drawpad.move(oval, 10, 0)
	

#__init__()	
#button1Click()
#button2Click()		
myapp = MyApp(root)
root.mainloop()