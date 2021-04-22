import re
import os
from tkinter import *
from time import sleep as s
import requests
import time
from PIL import ImageTk
def test_button():
    try:
        label['text'] = 'Connecting'
        req = requests.get('http://127.0.0.1:13081/')
        with open(r"C:\Users\owenw\Downloads\Answers.html", 'w', encoding='utf-8') as file:
            file.write(re.sub(
                r'<hr /> Proudly powered by OFF \| <a href=\"https://t.me/offhax\">Telegram</a> \| 100\% Free\!', '', req.text))
        label['text'] = 'Done'
        label1['text'] = 'No error message'
        root.after(1000, lambda: label.configure(text='Not Started'))
        os.startfile(r'C:\Users\owenw\Downloads')
    except Exception as e:
        label['text'] = 'Error'
        label1['text'] = e


root = Tk()

canvas = Canvas(root, height=350, width=700)
canvas.pack()

background_image = ImageTk.PhotoImage(file=r"C:\Users\owenw\Downloads\image.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = Button(frame, text='Hack', font=40, command=lambda: test_button()) 
button.place(relx=0.5, relheight=1, relwidth=0.1, anchor='n')
button.counter = 0

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

button1 = Button(lower_frame, text='Quit', font=40,
                 command=lambda: root.quit())
button1.pack(side='bottom')

label = Label(lower_frame, text='Not Started')
label.place(relx=0.50, rely=0.10, relwidth=0.2, relheight=0.2, anchor='n')

label1 = Label(lower_frame, text='No error message')
label1.place(relx=0.50, rely=0.50, relwidth=0.7, relheight=0.16, anchor='n')
root.eval('tk::PlaceWindow . center')
root.mainloop()
