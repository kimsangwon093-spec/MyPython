import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(400, 300, image=photo[pnum], tag="PH")
    pnum = pnum  + 1
    if pnum >= len(photo):
        pnum = 0
    root.after(1000, photograph)

root = tkinter.Tk()
root.title("바디 갤러리")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
photo = [
tkinter.PhotoImage(file="body_1.png"),
tkinter.PhotoImage(file="body_2.png"),
tkinter.PhotoImage(file="body_3.png"),
tkinter.PhotoImage(file="body_4.png"),
tkinter.PhotoImage(file="body_5.png"),
tkinter.PhotoImage(file="body_6.png"),
tkinter.PhotoImage(file="body_7.png"),
tkinter.PhotoImage(file="body_8.png")
]
photograph()
root.mainloop()