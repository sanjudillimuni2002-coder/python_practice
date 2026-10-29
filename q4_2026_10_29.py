import tkinter as tk

root = tk.Tk()
root.title("red box disappeared")
root.geometry("600x300")

canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

box = canvas.create_rectangle(10, 100, 60, 150, fill="red")

def animation():
    canvas.move(box,5,0)
    root.after(50,animation)

def disappear(event):
    canvas.delete(box)

canvas.tag_bind(box, "<Button-1>", disappear)

animation()
root.mainloop()
