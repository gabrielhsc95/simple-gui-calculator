import tkinter as tk
import tkinter.font as tkFont


root = tk.Tk()
root.title("Calculator")

decimal = False
memory = 0

def click_number(number):
    if screen.get() == "ERROR":
        clear()
    screen.insert(tk.END, str(number))


def clear():
    screen.delete(0, tk.END)

def backspace():
    current = screen.get()
    clear()
    screen.insert(0, current[0:-1])

def decimal_case():
    if screen.get() == "ERROR":
        clear()

    if "." in screen.get():
        clear()
        screen.insert(0, "ERROR")
    else:
        screen.insert(tk.END, ".")

def add():
    if screen.get() == "":
        clear()
        screen.insert(0, "ERROR")
    else:
        try:
            current = int(screen.get())
        except:
            current = float(screen.get())
        global memory
        memory = current
        global operator
        operator = "+"
        clear()

def subtraction():
    if screen.get() == "":
        clear()
        screen.insert(0, "ERROR")
    else:
        try:
            current = int(screen.get())
        except:
            current = float(screen.get())
        global memory
        memory = current
        global operator
        operator = "-"
        clear()

def multiplication():
    if screen.get() == "":
        clear()
        screen.insert(0, "ERROR")
    else:
        try:
            current = int(screen.get())
        except:
            current = float(screen.get())
        global memory
        memory = current
        global operator
        operator = "*"
        clear()

def division():
    if screen.get() == "":
        clear()
        screen.insert(0, "ERROR")
    else:
        try:
            current = int(screen.get())
        except:
            current = float(screen.get())
        global memory
        memory = current
        global operator
        operator = "/"
        clear()

def result():
    try:
        current = int(screen.get())
    except:
        current = float(screen.get())

    if operator == "+":
        final = memory + current
    if operator == "-":
        final = memory - current
    if operator == "*":
        final = memory * current
    if operator == "/":
        if current == 0.0:
            clear()
            final = "ERROR"
        else:
            final = memory / current

    clear()
    screen.insert(0, str(final))


# Screen
screen = tk.Entry(width=25)
screen.grid(row=0, column=0, columnspan=4)

# Number buttons
button_0 = tk.Button(text="0", padx=20, pady=15, command=lambda: click_number(0))
button_0.grid(row=4, column=1)
button_1 = tk.Button(text="1", padx=20, pady=15, command=lambda: click_number(1))
button_1.grid(row=3, column=0)
button_2 = tk.Button(text="2", padx=20, pady=15, command=lambda: click_number(2))
button_2.grid(row=3, column=1)
button_3 = tk.Button(text="3", padx=20, pady=15, command=lambda: click_number(3))
button_3.grid(row=3, column=2)
button_4 = tk.Button(text="4", padx=20, pady=15, command=lambda: click_number(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(text="5", padx=20, pady=15, command=lambda: click_number(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(text="6", padx=20, pady=15, command=lambda: click_number(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(text="7", padx=20, pady=15, command=lambda: click_number(7))
button_7.grid(row=1, column=0)
button_8 = tk.Button(text="8", padx=20, pady=15, command=lambda: click_number(8))
button_8.grid(row=1, column=1)
button_9 = tk.Button(text="9", padx=20, pady=15, command=lambda: click_number(9))
button_9.grid(row=1, column=2)

# Operation buttons
button_add = tk.Button(text="+", padx=20, pady=15, command=add)
button_add.grid(row=4, column=3)
button_subtract = tk.Button(text="-", padx=20, pady=15, command=subtraction)
button_subtract.grid(row=3, column=3)
button_multiply = tk.Button(text="x", padx=20, pady=15, command=multiplication)
button_multiply.grid(row=2, column=3)
button_division = tk.Button(text="÷", padx=20, pady=15, command=division)
button_division.grid(row=1, column=3)

# Other buttons
button_equals = tk.Button(text="=", padx=40, pady=15, command=result)
button_equals.grid(row=5, column=2, columnspan=2)
button_dot = tk.Button(text=".", padx=20, pady=15, command=decimal_case)
button_dot.grid(row=4, column=2)
button_del = tk.Button(text="<", padx=20, pady=15, command=backspace)
button_del.grid(row=5, column=0)
button_clear = tk.Button(text="C", padx=20, pady=15, command=clear)
button_clear.grid(row=5, column=1)

root.mainloop()

