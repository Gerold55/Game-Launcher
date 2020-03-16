from tkinter import *



def create_window():
    window = Tk()

def button_callback():
    print('Hello World')

if __name__ == '__main__':
    window = create_window()
    # Rest of code goes here
	
	
	
	
	
b = Button(window, text="News", command=button_callback)
b.pack()
	
	# add title
window.title("Phoenix Launcher")
	# set frame & geometry (widthxheight+XPOS+YPOS)
window.geometry("1000x600+100+200")
window.mainloop()
