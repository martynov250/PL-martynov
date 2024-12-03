import json
import requests
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Мартынов Михаил Владимирович')
window.geometry('700x400')
tab_control = ttk.Notebook(window)

lbl = Label(window, text='Введите название')
lbl.grid(column=0, row=0)

txt = Entry(window, width=30)
txt.grid(column=0, row=1)

text = Text(window, width=50, height=20, bg='white', fg='blue', wrap=WORD)

text.grid(column=0, row=3)

def clicked():
    username = txt.get()
    url1 = f'https://api.github.com/users/{username}'
    user_data = requests.get(url1).json()
    fi = user_data

    dict = {
        'company' : fi.get('company'),
        'created_at' : fi.get('created_at'),
        'email' : fi.get('email'),
        'id' : fi.get('id'),
        'name' : fi.get('name'),
        'url' : fi.get('url')
        }
    with open('text.json','w') as file:
        json.dump(dict, file, indent=4)
    text.delete(1.0, END)
    text.insert(END, dict)

btn = Button(window, text="открыть", command=clicked)
btn.grid(column=0, row=2)

window.mainloop()
