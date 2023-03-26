import tkinter as tk
from tkinter import ttk
from calculator import Calculator
import logging 

def button_press(entry):
    if entry in [str(n) for n in range(0, 10)]:
        c.add_to_expression(entry)
    elif entry in ['+', '-', '*', '/', '(', ')', '.']:
        c.add_to_expression(entry)
    elif entry == 'clear':
        c.clear()
    elif entry == 'delete':
        c.delete()
    elif entry == '=':
        c.equals()

    expression.set(c.expression)

def widgets():
    ttk.Entry(frame, textvariable=expression).grid(columnspan=5, ipadx=90)

    ttk.Button(frame, text="(", command=lambda: button_press("(")).grid(column=1, row=1)
    ttk.Button(frame, text=")", command=lambda: button_press(")")).grid(column=2, row=1)
    ttk.Button(frame, text="Clear", command=lambda: button_press("clear")).grid(column=3, row=1)
    ttk.Button(frame, text="Delete", command=lambda: button_press("delete")).grid(column=4, row=1)

    ttk.Button(frame, text="7", command=lambda: button_press("7")).grid(column=1, row=2)
    ttk.Button(frame, text="8", command=lambda: button_press("8")).grid(column=2, row=2)
    ttk.Button(frame, text="9", command=lambda: button_press("9")).grid(column=3, row=2)
    ttk.Button(frame, text="/", command=lambda: button_press("/")).grid(column=4, row=2)

    ttk.Button(frame, text="4", command=lambda: button_press("4")).grid(column=1, row=3)
    ttk.Button(frame, text="5", command=lambda: button_press("5")).grid(column=2, row=3)
    ttk.Button(frame, text="6", command=lambda: button_press("6")).grid(column=3, row=3)
    ttk.Button(frame, text="*", command=lambda: button_press("*")).grid(column=4, row=3)

    ttk.Button(frame, text="1", command=lambda: button_press("1")).grid(column=1, row=4)
    ttk.Button(frame, text="2", command=lambda: button_press("2")).grid(column=2, row=4)
    ttk.Button(frame, text="3", command=lambda: button_press("3")).grid(column=3, row=4)
    ttk.Button(frame, text="-", command=lambda: button_press("-")).grid(column=4, row=4)

    ttk.Button(frame, text="0", command=lambda: button_press("0")).grid(column=1, row=5)
    ttk.Button(frame, text=".", command=lambda: button_press(".")).grid(column=2, row=5)
    ttk.Button(frame, text="=", command=lambda: button_press("=")).grid(column=3, row=5)
    ttk.Button(frame, text="+", command=lambda: button_press("+")).grid(column=4, row=5)

def bindings():
    window.bind('<Escape>', lambda f: window.destroy())
    window.bind('<KeyRelease>', lambda f: c.update_expression(expression.get()))
    window.bind('<Return>', lambda f: button_press("="))
 
if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    c = Calculator()
    
    window = tk.Tk()
    window.title("Calculator")
    frame = ttk.Frame(window, padding=10)
    frame.grid()
    
    expression = tk.StringVar()
    widgets()
    bindings()
    
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    window.mainloop()