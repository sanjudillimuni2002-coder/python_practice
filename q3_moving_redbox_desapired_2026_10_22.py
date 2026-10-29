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

def click_box(event):#if i click box it will run
    canvas.delete(box)#red box disapired


canvas.tag_bind(box, "<Button-1>", click_box)


animation()

root.mainloop()


#tag_bind() → Box එකට Mouse event එකක් සම්බන්ධ කරනවා.

#"<Button-1>" → Mouse එකේ වම් බොත්තම Click කිරීම.

#click_box → Click කළ විට ක්‍රියාත්මක කළ යුතු function එක.
