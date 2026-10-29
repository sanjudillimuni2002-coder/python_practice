
import tkinter as tk

root = tk.Tk()
root.title("Red Box Move")
root.geometry("600x300")#window width hight

#box moving space
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

#creat red box
box = canvas.create_rectangle(10, 100, 60, 150, fill="red")

def animation():
    canvas.move(box, 5, 0)#move box 5px
    root.after(50, animation)#move box after 50milisecond


animation()

root.mainloop()



