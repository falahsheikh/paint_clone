#import to use functions
from tkinter import*

currnet_x, current_y = 0, 0
colour = 'black'

# find the x, y coodrinates of the users CLICK
def locate_xy(event):
    global current_x,current_y
    current_x, current_y = event.x, event.y
# find the x, y coordinates of the users DRAG
def addLine(event):
    global current_x, current_y
                                                                # changing the lines colour to 'colour'
    canvas.create_line((current_x, current_y, event.x, event.y), fill = colour)
    # because it only draws from the starting point
    current_x, current_y = event.x, event.y

def show_colour(new_colour):
    global colour
    colour = new_colour
# makes a new canvas
def new_canvas():
    canvas.delete('all')
    display_pallete()



# this opens a plain GUI
window = Tk()
# changes title from 'tk' to 'Paint Lab'
window.title('Paint Lab')
# full screen/screen
window.state('zoomed')

# inset grid
# 'weight=1' ensures the row/column reaches the sides when screen is expanded
window.rowconfigure(0,weight=1)
window.columnconfigure(0, weight=1)

# creating a menu bar
menubar = Menu(window)
window.config(menu = menubar)
submenu = Menu(menubar)

menubar.add_cascade(label = 'File', menu = submenu)
submenu.add_command(label = 'New Canvas', command = new_canvas)

# to place atop the window
canvas=Canvas(window, background = 'white')

# placed on the grid
canvas.grid(row=0,column=0, sticky='nsew') # nsew = NorthSouthEastWest; allows canvas to reach all the sides


# canvas.create_line(20,20,60,20) # represent coordinates; parameter
# this allows the user to find the coordinates of where he/she CLICKED
canvas.bind('<Button-1>', locate_xy)
# this allows the user to find the coordinates of where he/she DRAGGED
canvas.bind('<B1-Motion>', addLine)

def display_pallete():
    # creating the pallete
    id = canvas.create_rectangle(10, 10, 30, 30, fill = 'black')
    # tag bind                        # lambda to call a funtion
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('black'))
    id = canvas.create_rectangle(10, 40, 30, 60, fill = 'white')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('white'))
    id = canvas.create_rectangle(10, 70, 30, 90, fill = 'red')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('red'))
    id = canvas.create_rectangle(10, 100, 30, 120, fill = 'orange')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('orange'))
    id = canvas.create_rectangle(10, 130, 30, 150, fill = 'yellow')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('yellow'))
    id = canvas.create_rectangle(10, 160, 30, 180, fill = 'green')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('green'))
    id = canvas.create_rectangle(10, 190, 30, 210, fill = 'blue')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('blue'))
    id = canvas.create_rectangle(10, 220, 30, 240, fill = 'purple')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('purple'))
    id = canvas.create_rectangle(10, 250, 30, 270, fill = 'grey')
    canvas.tag_bind(id, '<Button-1>', lambda x: show_colour('grey'))

display_pallete()

window.grid_columnconfigure(0,weight=1)

# makes sure the window is running correctly
window.mainloop()