from tkinter import *
from tkinter import ttk, filedialog, messagebox, Radiobutton
from tkinter import Menu
from tkinter.ttk import Combobox

# создание окна
window = Tk()
window.title('Мартынов Михаил Владимирович')
window.geometry('700x400')
tab_control = ttk.Notebook(window)



# калькулятор
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

txt = Entry(tab1, width=10)
txt.grid(column=0, row=0)
combo = Combobox(tab1)
combo['values'] = ('/', '*', '-', '+')
combo.current(0)
combo.grid(column=1, row=0)
txt1 = Entry(tab1, width=10)
txt1.grid(column=2, row=0)
lbl = Label(tab1, text='=')
lbl.grid(column=3, row=0)

# ошибки в употреблении символов
def clicka():
    messagebox.showerror('error', 'недопустмимые знаки в первом числе')
def clicka_():
    messagebox.showerror('error', 'нет первого числа')
def clickb():
    messagebox.showerror('error', 'недопустмимые знаки во втором числе')
def clickb_():
    messagebox.showerror('error', 'нет второго числа')

# функция калькулятора
def clicked():
    ka = 0
    la = 0
    kb = 0
    lb = 0
    a = txt.get()
    b = txt1.get()
    c = combo.get()
    str(a)
    str(b)

# исключения для всего числа a
    for i in range(len(a)):
        if a[i] != '0':
            if a[i] != '1':
                if a[i] != '2':
                    if a[i] != '3':
                        if a[i] != '4':
                            if a[i] != '5':
                                if a[i] != '6':
                                    if a[i] != '7':
                                        if a[i] != '8':
                                            if a[i] != '9':
                                                if a[i] != '.':
                                                    if a[i] != '-':
                                                        print(clicka())
# исключение первой точки и пустоты в a
    for i in range(len(a)):
        if a[0] == '.':
            print(clicka())
    for i in range(len(a)):
        if a[i] == '.':
            ka = ka + 1
            if ka > 1:
                print(clicka())
    if a == '':
        print(clicka_())
# исключение минуса в a
    for i in range(len(a)):
        if a[i] == '-':
            la = la + 1
            if la > 1:
                print(clicka())
    for i in range(len(a)):
        if (a[i] == '-') and (len(a) == 1):
            print(clicka())

# исключения для всего числа b
    for i in range(len(b)):
        if b[i] != '0':
            if b[i] != '1':
                if b[i] != '2':
                    if b[i] != '3':
                        if b[i] != '4':
                            if b[i] != '5':
                                if b[i] != '6':
                                    if b[i] != '7':
                                        if b[i] != '8':
                                            if b[i] != '9':
                                                if b[i] != '.':
                                                    if b[i] != '-':
                                                        print(clickb())
# исключение первой точки и пустоты в b
    for i in range(len(b)):
        if b[0] == '.':
            print(clickb())
    for i in range(len(b)):
        if b[i] == '.':
            kb = kb + 1
            if kb > 1:
                print(clickb())
    if b == '':
        print(clickb_())
# исключение минуса в b
    for i in range(len(b)):
        if b[i] == '-':
            lb = lb + 1
            if lb > 1:
                print(clickb())
    for i in range(len(b)):
        if (b[i] == '-') and (len(b) == 1):
            print(clickb())

# деление
    if c == "/":
# условие деления на 0
        if b == '0':
            messagebox.showerror('error', 'делить на 0 нельзя')
        d = float(a) / float(b)
        lbl.configure(text=d)
        lbl.grid(column=5, row=0)
# умножение
    if c == "*":
        d = float(a) * float(b)
        lbl.configure(text=d)
        lbl.grid(column=5, row=0)
# вычитание
    if c == "-":
        d = float(a) - float(b)
        lbl.configure(text=d)
        lbl.grid(column=5, row=0)
# сложение
    if c == "+":
        d = float(a) + float(b)
        lbl.configure(text=d)
        lbl.grid(column=5, row=0)

btn = Button(tab1, text="равно", command=clicked)
btn.grid(column=0, row=1)



# чекбокс
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')
# функции чекбокса
def clicked21():
    messagebox.showinfo('information', 'Вы выбрали первый вариант')
def clicked22():
    messagebox.showinfo('information', 'Вы выбрали второй вариант')
def clicked23():
    messagebox.showinfo('information', 'Вы выбрали третий вариант')

rad1 = Radiobutton(tab2, text='Первый', value=1, command=clicked21)
rad2 = Radiobutton(tab2, text='Второй', value=2, command=clicked22)
rad3 = Radiobutton(tab2, text='Третий', value=3, command=clicked23)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)



# работа с текстом
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Текст')

def read():
    file = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file:
        with open(file, 'r') as file:
            content = file.read()
            text.delete(1.0, END)
            text.insert(END, content)

menu = Menu(window)
window.config(menu=menu)


podmenu = Menu(menu, tearoff=0)
podmenu.add_command(label='загрузить текст', command=read)
menu.add_cascade(label='файл', menu=podmenu)


text = Text(tab3, width=50, height=10, bg='white', fg='blue', wrap=WORD)
text.pack(expand=1, fill='both')


tab_control.pack(expand=1, fill='both')
window.mainloop()