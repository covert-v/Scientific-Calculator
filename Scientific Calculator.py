
#Project Name:  Calculator
#Codebase by:   Covert-v

#Project Description: a scientific calculator built entirely on python with customtkinter as the GUI


import customtkinter as ctk
import math


#Window Setup
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Scientific Calculator')
app.geometry('600x760')

#Global Variables Setup
first_number = ''
operator = ''
last_clicked = ''

#Arithmetic Display
expr_label = ctk.CTkLabel(app, text='', font=('Arial', 16), text_color='gray')
expr_label.pack(anchor='e', padx=25)

#Number Display Setup
display = ctk.CTkEntry(app, font = ('Arial', 32), width = 560, justify = 'right')
display.pack(pady = 20)
display.insert(0, '0')

#Button Layout
buttons = [
    ['⌫',   'C',    '%',    '÷'],
    ['7',   '8',    '9',    '×'],
    ['4',   '5',    '6',    '−'],
    ['1',   '2',    '3',    '+'],
    ['+/-', '0',    '.',    '='],
    ['sin', 'cos',  'tan',  '√'],
    ['x²',  'xʸ',   'log',  'ln'],
]

#Button Layout Setup
btn_frame = ctk.CTkFrame(app)
btn_frame.pack()

for row_x, row in enumerate(buttons):
    for col_x, label in enumerate(row):
        btn = ctk.CTkButton(btn_frame, text = label, width = 130, height = 80, font = ('Arial', 24), corner_radius = 45, command = lambda l = label: on_click(l))
        btn.grid(row = row_x, column = col_x, padx = 5, pady = 5)


#Pulls What's Currently On Display
def get_display():
    return display.get()

#Changes Display
def set_display(value):
    display.delete(0, 'end')
    display.insert(0, value)

#Specific Response Depending On What's Clicked
def on_click(label):
    global first_number, operator, last_clicked
    
#Clears The Display If Arithmetic Was Completed On Last Click    
    if last_clicked == '=' and label.isdigit():
        set_display(label)
        first_number = ''
        operator = ''
        expr_label.configure(text='')

#Clear Button
    elif label == 'C':
        set_display('0')
    
#Arithmetic Requiring A Second Variable
    elif label in ['+', '−', '×', '÷', '%', 'xʸ']:
        first_number = get_display()
        operator = label
        set_display('0')
        expr_label.configure(text=f'{first_number} {operator}')

#Arithmetic That Doesn't Require A Second Variable
    elif label == 'sin':
        current = get_display()
        result = math.sin(math.radians(float(get_display())))
        set_display(str(result))

    elif label == 'cos':
        current = get_display()
        result = math.cos(math.radians(float(get_display())))
        set_display(str(result))

    elif label == 'tan':
        current = get_display()
        result = math.tan(math.radians(float(get_display())))
        set_display(str(result))

    elif label == '√':
        current = get_display()
        if float(current) < 0:
            set_display('Error')
        else:
            result = math.sqrt(float(get_display()))
            set_display(str(result))

    elif label == 'x²':
        current = get_display()
        result = float(current) * float(current)
        set_display(str(result))           

    elif label == 'log':
        current = get_display()
        if float(current) <= 0:
            set_display('Error')
        else:
            result = math.log10(float(get_display()))
            set_display(str(result))  

    elif label == 'ln':
        current = get_display()
        if float(current) <= 0:
            set_display('Error')
        else:
            result = math.log(float(get_display()))
            set_display(str(result))  

    elif label == '+/-':
        current = float(get_display())
        set_display(str(int(-current) if -current == int(-current) else -current))
    

#Equals Button
    elif label == '=':
        second_number = get_display()
        if operator == '+':
            result = float(first_number) + float(second_number)
            set_display(str(int(result) if result == int(result) else result))
        elif operator == '−':
            result = float(first_number) - float(second_number)
            set_display(str(int(result) if result == int(result) else result))
        elif operator == '×':
            result = float(first_number) * float(second_number)
            set_display(str(int(result) if result == int(result) else result))
        elif operator == '÷':
            if float(second_number) == 0:
                set_display('Error')
            else:
                result = float(first_number) / float(second_number)
                set_display(str(int(result) if result == int(result) else result))
        elif operator == '%':
            result = (float(first_number)/100)*float(second_number)
            set_display(str(int(result) if result == int(result) else result))
        elif operator == 'xʸ':
            result = float(first_number)**float(second_number)
            set_display(str(result))
        expr_label.configure(text='') 

#Backspace Button
    elif label == '⌫':
        current = get_display()
        result = current[:-1]
        if not result:
            set_display('0')
        else:
            set_display(result)

#For When 0 Is On Display    
    elif get_display() == '0':
        set_display(label)
    
#For When Zero Is Not On Display
    else:
        current = get_display()
        set_display(current + label)

#Updates The Last Clicked Variable
    last_clicked = label

#Starting The Loop
app.mainloop()