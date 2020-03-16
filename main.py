from tkinter import *



def createWindow():
	window = Tk()
	
	# add widget here
	b = Button(window, text="News")
	b = Button(window, text="ModStore")
	b = Button(window, text="Games/Modpacks/Saves")
	b = Button(window, text="Worlds")
	b = Button(window, text="Servers")
	b.pack()
	
	# add title
	window.title("Phoenix Launcher")
	# set frame & geometry (widthxheight+XPOS+YPOS)
	window.geometry("1000x600+100+200")
	window.mainloop()
	

if __name__ == '__main__':
	createWindow()
	
	
	
	
	
	