#!/usr/bin/env python
#coding:utf-8

from Tkinter import *

def Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self,test='Hello,world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		sellf.quitbutton.pack()
	
	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message','Hello, %s' % name)


app = Application()
app.master.title('Hello World')
app.mainloop()
