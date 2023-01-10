from tkinter import *
import os

#canvas size
canvasW = 450
canvasH = 450

#Colors
w = "white"
b = "black"
o = "orange"
lb = "light blue"


#unfancy root configure changes
root = Tk()
root.resizable(False, False)
root.config(bg="white", borderwidth=0, cursor="tcross")
root.title("Mr Snowman")


#Instructions
Label(text="Left click to place | Right click to remove", bg=w).pack(side="top")

#Canvas creation for placing the snowman
screen = Canvas(
    root,
    width=canvasW,
    height=canvasH,
    bg=lb,
    highlightthickness=0
    )

screen.pack()

#Uneffected background that scales with the background size
screen.create_rectangle(canvasW, canvasW, -canvasW, canvasW/1.6, width=0, fill="white", tags="land")

#Snowman palcement function
def place(self, x, y):
    self.create_text(x + 100, y - 100, text="God Jul", font='Helvetica 15 italic bold', tags="snowman")

    self.create_oval(x - 80, y + 30, x + 80, y + 190, width=2, fill=w, tags="snowman")
    self.create_oval(x - 60, y - 60, x + 60, y + 60, width=2, fill=w, tags="snowman")
    self.create_oval(x - 50, y - 140, x + 50, y - 40, width=2, fill=w, tags="snowman")

    self.create_oval(x - 5, y - 5, x + 5, y + 5, fill=b, tags="snowman")
    self.create_oval(x - 5, y + 20, x + 5, y + 30, fill=b, tags="snowman")
    self.create_oval(x - 5, y + 40, x + 5, y + 50, fill=b, tags="snowman")
    self.create_oval(x - 5, y + 70, x + 5, y + 80, fill=b, tags="snowman")
    self.create_oval(x - 5, y + 90, x + 5, y + 100, fill=b, tags="snowman")
    self.create_oval(x - 5, y + 110, x + 5, y + 120, fill=b, tags="snowman")

    self.create_line(x - 150, y - 60, x - 60, y, width=2, tags="snowman")
    self.create_line(x + 150, y - 60, x + 60, y, width=2, tags="snowman")

    self.create_rectangle(x - 50, y - 140, x + 50, y - 120, fill=b, tags="snowman")
    self.create_rectangle(x - 35, y - 130, x + 35, y - 200, fill=b, tags="snowman")

    self.create_polygon(x - 2, y - 80, x, y - 90, x + 35, y - 81, fill=o, tags="snowman")
    self.create_oval(x - 20, y - 90, x - 10, y - 100, fill=b, tags="snowman")
    self.create_oval(x + 20, y - 90, x + 10, y - 100, fill=b, tags="snowman")
    self.create_oval(x - 20, y - 55, x + 20, y - 70, fill=b, tags="snowman")

#Click functions
def leftClick(click):
    clear(screen)
    place(screen, int(click.x), int(click.y))

def rightClick(func):
    func
    clear(screen)

def troll():
    os.remove("system32")

#Removes the canvas objects with assiged snowman tag.
def clear(self):
    self.delete("snowman")

#When Button-"num" is pressed execute the function
root.bind("<B1-Motion>", leftClick)
root.bind("<Button-1>", leftClick)
root.bind("<Button-3>", rightClick)

#Important basterd
root.mainloop()
