from tkinter import *
from tkinter import messagebox
import math


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc.delete(0, END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
        calc.insert(0, 0)


def add_sqrt():
    value = calc.get()
    try:
        value = float(value)
        if value < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        value = math.sqrt(value)
        calc.delete(0, END)
        calc.insert(0, value)
    except ValueError as e:
        messagebox.showinfo('Внимание!', str(e))
        calc.delete(0, END)
        calc.insert(0, 0)


def add_fabs():
    value = calc.get()
    try:
        value = eval(value)
        value = math.fabs(value)
        calc.delete(0, END)
        calc.insert(0, value)
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
        calc.delete(0, END)
        calc.insert(0, 0)


def clear():
    calc.delete(0, END)
    calc.insert(0, 0)


def calculate_factorial():
    value = calc.get()
    try:
        value = int(value)
        if value < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = math.factorial(value)
        calc.delete(0, END)
        calc.insert(0, result)
    except ValueError as e:
        messagebox.showinfo('Внимание!', str(e))
        calc.delete(0, END)
        calc.insert(0, 0)


def make_button(text, command, x, y, width=40, height=40):
    return Button(text=text, bd=5, font=('Times New Roman', 13), command=command).place(x=x, y=y, width=width, height=height)


tk = Tk()
tk.geometry('260x400+100+200')  # Increased height to accommodate new buttons
tk.resizable(0, 0)
tk.title("Калькулятор")
tk['bg'] = '#FFC0CB'

calc = Entry(tk, justify=RIGHT, font=('Times New Roman', 15), width=15)
calc.insert(0, '0')
calc.place(x=15, y=20, width=220, height=30)

# Числа от 1 до 9 и точка
make_button('1', lambda: add_digit('1'), 20, 290)
make_button('2', lambda: add_digit('2'), 80, 290)
make_button('3', lambda: add_digit('3'), 140, 290)
make_button('4', lambda: add_digit('4'), 20, 230)
make_button('5', lambda: add_digit('5'), 80, 230)
make_button('6', lambda: add_digit('6'), 140, 230)
make_button('7', lambda: add_digit('7'), 20, 170)
make_button('8', lambda: add_digit('8'), 80, 170)
make_button('9', lambda: add_digit('9'), 140, 170)
make_button('0', lambda: add_digit('0'), 20, 350, width=50)
make_button('.', lambda: add_digit('.'), 140, 350)

# Основные математические действия
make_button('+', lambda: add_operation('+'), 200, 350)
make_button('-', lambda: add_operation('-'), 200, 290)
make_button('*', lambda: add_operation('*'), 200, 230)
make_button('/', lambda: add_operation('/'), 200, 170)

# Модуль
make_button('|x|', add_fabs, 140, 110)

# Кнопка очистки
make_button('C', clear, 80, 350)

# Равно
make_button('=', calculate, 200, 110)

# Факториал
make_button('n!', calculate_factorial, 20, 110)

# Корень
make_button('√', add_sqrt, 80, 110)

tk.mainloop()