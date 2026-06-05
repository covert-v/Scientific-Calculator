
#Project Name:  Calculator
#Codebase by:   Covert-v

#Project Description: a scientific calculator built entirely on python with customtkinter as the GUI


import customtkinter as ctk
import math

ctk.set_appearance_mode('light')


class ScientificCalculator(ctk.CTk):

    OPERATORS =     {'+', '−', '×', '÷', '='}
    UTILITY =       {'⌫', 'C', '+/-', '%'}
    SCIENTIFIC =    {'sin', 'cos', 'tan', '√', 'x²', 'xʸ', 'log', 'ln'}

    KEY_MAP = {
        'Return': '=',      'KP_Enter': '=',
        'BackSpace': '⌫',   'Escape': 'C',
        'KP_Add': '+',      'KP_Subtract': '−',
        'KP_Multiply': '×', 'KP_Divide': '÷',
        'KP_Decimal': '.',  'KP_0': '0', 'KP_1': '1', 'KP_2': '2',
        'KP_3': '3', 'KP_4': '4', 'KP_5': '5', 'KP_6': '6',
        'KP_7': '7', 'KP_8': '8', 'KP_9': '9',
    }
    CHAR_MAP = {
        **{str(i): str(i) for i in range(10)},
        '.': '.', '+': '+', '-': '−', '*': '×', '/': '÷',
        '=': '=', '%': '%',
    }

    def __init__(self):
        super().__init__()
        self.title('Scientific Calculator')
        self.configure(fg_color='#FDF4EE')

        self.first_number = ''
        self.operator     = ''
        self.last_clicked = ''
        self.use_degrees  = True
        self.history      = []

        # Frame of Calculator

        panel = ctk.CTkFrame(self, fg_color='#FAF0E8', corner_radius=24,
                             border_width=1, border_color='#EDD8C8')
        panel.pack(fill='both', expand=True, padx=10, pady=10)

        # History Label

        self.history_label = ctk.CTkLabel(
            panel, text='', font=('Arial', 11), text_color='#A08070',
            anchor='e', justify='right', width=450, height=36,
            fg_color='#FFFCF9', corner_radius=10
        )
        self.history_label.pack(pady=(10, 2), padx=22)

        # Expression Labels

        self.expr_label = ctk.CTkLabel(panel, text='', font=('Arial', 13),
                                       text_color='#A08070', height=18)
        self.expr_label.pack(anchor='e', padx=24, pady=0)

        # Number Display 

        self.display = ctk.CTkEntry(
            panel, font=('Arial', 34), width=450, justify='right',
            fg_color='#FFFCF9', border_color='#EDD8C8', border_width=1,
            text_color='#5C3D2E', corner_radius=12
        )
        self.display.pack(pady=(3, 4), padx=22)
        self.display.insert(0, '0')
        self.display.bind('<Button-1>', self._copy_to_clipboard)

        # DEG/RAD Toggle

        bar = ctk.CTkFrame(panel, fg_color='transparent')
        bar.pack(fill='x', padx=22, pady=(0, 4))

        self.deg_rad_btn = ctk.CTkButton(
            bar, text='DEG', width=60, height=24,
            font=('Arial', 12), corner_radius=12,
            fg_color='#F2D5C4', hover_color='#EAC8B0',
            text_color='#5C3D2E', border_width=0,
            command=self._toggle_deg_rad
        )
        self.deg_rad_btn.pack(side='left')

        self.copy_hint = ctk.CTkLabel(bar, text='', font=('Arial', 11),
                                      text_color='#A08070')
        self.copy_hint.pack(side='right')

        # Button Grid
        buttons = [
            ['⌫',   'C',    '%',    '÷'],
            ['7',   '8',    '9',    '×'],
            ['4',   '5',    '6',    '−'],
            ['1',   '2',    '3',    '+'],
            ['+/-', '0',    '.',    '='],
            ['sin', 'cos',  'tan',  '√'],
            ['x²',  'xʸ',   'log',  'ln'],
        ]

        btn_frame = ctk.CTkFrame(panel, fg_color='transparent')
        btn_frame.pack(padx=14, pady=(0, 14))

        for row_x, row in enumerate(buttons):
            for col_x, label in enumerate(row):
                style = self._button_style(label)
                btn = ctk.CTkButton(
                    btn_frame, text=label, width=104, height=60,
                    font=('Arial', 19), corner_radius=30,
                    command=lambda l=label: self.on_click(l),
                    **style
                )
                btn.grid(row=row_x, column=col_x, padx=3, pady=3)

        self.bind('<Key>', self._on_key)
        self.display.bind('<Key>', self._on_key)

        self.update_idletasks()
        self.geometry('510x655')
        self.resizable(False, False)

    # GUI Design

    def _button_style(self, label):
        if label in self.OPERATORS:
            return {'fg_color': '#D4826A', 'hover_color': '#C07058',
                    'text_color': '#FFFFFF', 'border_width': 0}
        if label in self.UTILITY:
            return {'fg_color': '#F2D5C4', 'hover_color': '#EAC8B0',
                    'text_color': '#5C3D2E', 'border_width': 0}
        if label in self.SCIENTIFIC:
            return {'fg_color': '#EDE0F0', 'hover_color': '#E4D4EC',
                    'text_color': '#5C3D2E', 'border_color': '#DDD0E8',
                    'border_width': 1}
        return {'fg_color': '#FFFCF9', 'hover_color': '#FAF0E8',
                'text_color': '#5C3D2E', 'border_color': '#EDD8C8',
                'border_width': 1}

    # Display Functions

    def get_display(self):
        return self.display.get().replace(',', '')

    def set_display(self, value):
        str_val = str(value).replace(',', '')
        try:
            if str_val == 'Error' or 'e' in str_val.lower():
                formatted = str_val
            elif str_val.endswith('.'):
                formatted = f'{int(str_val[:-1]):,}.'
            elif '.' in str_val:
                int_part, dec_part = str_val.split('.')
                formatted = f'{int(int_part):,}.{dec_part}'
            else:
                formatted = f'{int(str_val):,}'
        except (ValueError, TypeError):
            formatted = str_val
        self.display.delete(0, 'end')
        self.display.insert(0, formatted)

    def _format_result(self, result):
        """Round to 10 sig figs to hide floating-point noise; keep integers clean."""
        if result == int(result) and abs(result) < 1e15:
            return str(int(result))
        return f'{result:.10g}'

    # History Feature

    def _add_to_history(self, expression, result):
        self.history.append(f'{expression} = {result}')
        self.history_label.configure(text='\n'.join(self.history[-2:]))

    # Deg/Rad Feature

    def _toggle_deg_rad(self):
        self.use_degrees = not self.use_degrees
        self.deg_rad_btn.configure(text='DEG' if self.use_degrees else 'RAD')

    #Copy to Clipboard Feature

    def _copy_to_clipboard(self, _event=None):
        self.clipboard_clear()
        self.clipboard_append(self.get_display())
        self.copy_hint.configure(text='Copied!')
        self.after(1500, lambda: self.copy_hint.configure(text=''))

    #Enables Keyboard Entries

    def _on_key(self, event):
        label = self.KEY_MAP.get(event.keysym) or self.CHAR_MAP.get(event.char)
        if label:
            self.on_click(label)
        return 'break'

    # Main Functions Below

    def on_click(self, label):

    #Clears The Display If Arithmetic Was Completed On Last Click
        if self.last_clicked == '=' and label.isdigit():
            self.set_display(label)
            self.first_number = ''
            self.operator     = ''
            self.expr_label.configure(text='')

    #Clear Button
        elif label == 'C':
            self.set_display('0')
            self.first_number = ''
            self.operator     = ''
            self.expr_label.configure(text='')

    #Arithmetic Requiring A Second Variable
        elif label in ['+', '−', '×', '÷', 'xʸ']:
            self.first_number = self.get_display()
            self.operator     = label
            self.set_display('0')
            self.expr_label.configure(text=f'{self.first_number} {self.operator}')

    #Trig Functions
        elif label == 'sin':
            current = self.get_display()
            angle   = float(current)
            result  = math.sin(math.radians(angle) if self.use_degrees else angle)
            fmt     = self._format_result(result)
            self._add_to_history(f'sin({current})', fmt)
            self.set_display(fmt)

        elif label == 'cos':
            current = self.get_display()
            angle   = float(current)
            result  = math.cos(math.radians(angle) if self.use_degrees else angle)
            fmt     = self._format_result(result)
            self._add_to_history(f'cos({current})', fmt)
            self.set_display(fmt)

        elif label == 'tan':
            current = self.get_display()
            angle   = float(current)
            result  = math.tan(math.radians(angle) if self.use_degrees else angle)
            fmt     = self._format_result(result)
            self._add_to_history(f'tan({current})', fmt)
            self.set_display(fmt)

        elif label == '√':
            current = self.get_display()
            if float(current) < 0:
                self.set_display('Error')
            else:
                result = math.sqrt(float(current))
                fmt    = self._format_result(result)
                self._add_to_history(f'√({current})', fmt)
                self.set_display(fmt)

        elif label == 'x²':
            current = self.get_display()
            result  = float(current) ** 2
            fmt     = self._format_result(result)
            self._add_to_history(f'({current})²', fmt)
            self.set_display(fmt)

        elif label == 'log':
            current = self.get_display()
            if float(current) <= 0:
                self.set_display('Error')
            else:
                result = math.log10(float(current))
                fmt    = self._format_result(result)
                self._add_to_history(f'log({current})', fmt)
                self.set_display(fmt)

        elif label == 'ln':
            current = self.get_display()
            if float(current) <= 0:
                self.set_display('Error')
            else:
                result = math.log(float(current))
                fmt    = self._format_result(result)
                self._add_to_history(f'ln({current})', fmt)
                self.set_display(fmt)

        elif label == '%':
            current = float(self.get_display())
            if self.first_number and self.operator in ['+', '−']:
                result = (current / 100) * float(self.first_number)
            else:
                result = current / 100
            self.set_display(self._format_result(result))

        elif label == '+/-':
            current = float(self.get_display())
            self.set_display(self._format_result(-current))

    #Equals Button
        elif label == '=':
            second_number = self.get_display()
            result        = None

            if self.operator == '+':
                result = float(self.first_number) + float(second_number)
            elif self.operator == '−':
                result = float(self.first_number) - float(second_number)
            elif self.operator == '×':
                result = float(self.first_number) * float(second_number)
            elif self.operator == '÷':
                if float(second_number) == 0:
                    self.set_display('Error')
                else:
                    result = float(self.first_number) / float(second_number)
            elif self.operator == 'xʸ':
                result = float(self.first_number) ** float(second_number)

            if result is not None:
                fmt = self._format_result(result)
                self._add_to_history(
                    f'{self.first_number} {self.operator} {second_number}', fmt
                )
                self.set_display(fmt)

            self.expr_label.configure(text='')

    #Backspace Button
        elif label == '⌫':
            current = self.get_display()
            trimmed = current[:-1]
            self.set_display('0' if not trimmed else trimmed)

    #Prevent Double Decimal Point
        elif label == '.' and '.' in self.get_display():
            return

    #For When Zero Is On Display
        elif self.get_display() == '0':
            self.set_display(label)

    #For When Zero Is NOT On Display
        else:
            self.set_display(self.get_display() + label)

        self.last_clicked = label


if __name__ == '__main__':
    app = ScientificCalculator()
    app.mainloop()
