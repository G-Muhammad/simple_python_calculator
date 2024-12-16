from tkinter import *

first_number = second_number = operator = None
MAX_DIGITS = 15  # Adjusted for longer results

def get_digit(digit):
    if result_label['text'] == "Error":  # Reset after error
        result_label.config(text="")
    current = result_label['text']
    if len(current) < MAX_DIGITS:  # Restrict input length
        new = current + str(digit)
        result_label.config(text=new)
    adjust_font_size()

def clear():
    result_label.config(text='')
    adjust_font_size()

def get_operator(op):
    global first_number, operator
    if not result_label['text'].isdigit():
        result_label.config(text="Error")
        return
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator
    if not result_label['text'].isdigit():
        result_label.config(text="Error")
        return
    second_number = int(result_label['text'])
    if operator == '+':
        result = str(first_number + second_number)
    elif operator == '-':
        result = str(first_number - second_number)
    elif operator == '*':
        result = str(first_number * second_number)
    elif operator == '/':
        if second_number == 0:
            result_label.config(text="Error")
            return
        result = f"{first_number / second_number:.10g}"  # Float division
    if len(result) > MAX_DIGITS:
        result_label.config(text="Overflow")
    else:
        result_label.config(text=result)
    adjust_font_size()

def adjust_font_size():
    text_length = len(result_label['text'])
    font_size = 30 if text_length <= 10 else 20 if text_length <= 15 else 15
    result_label.config(font=('verdana', font_size, 'bold'))

def key_press(event):
    char = event.char
    if char.isdigit():
        get_digit(char)
    elif char in "+-*/":
        get_operator(char)
    elif char == '\r':  # Enter key
        get_result()
    elif char.lower() == 'c':
        clear()

root = Tk()
root.title("Simple_Calculator")
root.geometry('280x390')
root.resizable(0, 0)
root.configure(background='black')


result_label = Label(root, text='', bg='black', fg='white', anchor='e', width=15)
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 25), sticky='nsew')
result_label.config(font=('verdana', 30, 'bold'))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for (text, row, col) in buttons:
    if text.isdigit():
        btn = Button(root, text=text, bg='#00a65a', fg='red', command=lambda t=text: get_digit(t))
    elif text == 'C':
        btn = Button(root, text=text, bg='#00a65a', fg='red', command=clear)
    elif text == '=':
        btn = Button(root, text=text, bg='#00a65a', fg='red', command=get_result)
    else:
        btn = Button(root, text=text, bg='#00a65a', fg='red', command=lambda t=text: get_operator(t))
    btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
    btn.config(font=('verdana', 15, 'bold'))

root.bind("<Key>", key_press)

root.mainloop()
