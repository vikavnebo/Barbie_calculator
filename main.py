from tkinter import Tk, Frame, Button, Label, messagebox

from colors import *
from buttons import *
from Row import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('310x506')
        self.root.resizable(0, 0)
        self.root.title('Barbie Calculator')
        self.root.iconbitmap('calc.ico')

        self.main_frame = self.create_main_frame()
        self.result_frame = self.create_result_frame()

        self.total_expression = ''
        self.current_expression = ''
        self.total_lable, self.lable = self.create_lable()

    def create_main_frame(self):
        frame = Frame(self.root, bg=WHITE)
        frame.place(relwidth=1, relheight=1)
        return frame

    def create_result_frame(self):
        frame = Frame(self.root, bg=LIGHT_PINK, height=122)
        frame.place(relwidth=1, height=122)
        # frame.pack(expand=True, fill='both')
        return frame

    def create_lable(self):
        total_lable = Label(self.result_frame, text=self.total_expression, bg=LIGHT_PINK,
                            fg=WHITE, font=('Arial', 20))
        total_lable.place(x=14, y=18)

        lable = Label(self.result_frame, text=self.current_expression, bg=LIGHT_PINK,
                      fg=WHITE, font=('Arial', 32, 'bold'))
        lable.place(x=12, y=61)

        return total_lable, lable

    def initialize_interface(self):
        rows = []
        for row_number in range(5):
            rows.append(Row(row_number, Frame(self.main_frame, bg=WHITE)))

        rows[0].append_button(ButtonTypes.SIGN, '=', self.evaluate, width = 208)
        rows[0].append_button(ButtonTypes.SIGN, 'C', self.clear)

        rows[1].append_button(ButtonTypes.NUMBER, '1', lambda x = '1': self.add_to_expression(x))
        rows[1].append_button(ButtonTypes.NUMBER, '2', lambda x = '2': self.add_to_expression(x))
        rows[1].append_button(ButtonTypes.NUMBER, '3', lambda x = '3': self.add_to_expression(x))
        rows[1].append_button(ButtonTypes.SIGN, '+', lambda x = '+': self.append_operator(x))

        rows[2].append_button(ButtonTypes.NUMBER, '4', lambda x = '4': self.add_to_expression(x))
        rows[2].append_button(ButtonTypes.NUMBER, '5', lambda x = '5': self.add_to_expression(x))
        rows[2].append_button(ButtonTypes.NUMBER, '6', lambda x = '6': self.add_to_expression(x))
        rows[2].append_button(ButtonTypes.SIGN, '-', lambda x = '-': self.append_operator(x))

        rows[3].append_button(ButtonTypes.NUMBER, '7', lambda x = '7': self.add_to_expression(x))
        rows[3].append_button(ButtonTypes.NUMBER, '8', lambda x = '8': self.add_to_expression(x))
        rows[3].append_button(ButtonTypes.NUMBER, '9', lambda x = '9': self.add_to_expression(x))
        rows[3].append_button(ButtonTypes.SIGN, '\u00D7', lambda x = '*': self.append_operator(x))

        rows[4].append_button(ButtonTypes.SIGN, '.', lambda x = '.': self.add_to_expression(x))
        rows[4].append_button(ButtonTypes.NUMBER, '0', lambda x = '0': self.add_to_expression(x))
        rows[4].append_button(ButtonTypes.SIGN, '^', lambda x ='**': self.append_operator(x))
        rows[4].append_button(ButtonTypes.SIGN, '\u00F7', lambda x = '/': self.append_operator(x))

        for row in rows:
            row.place(pad=14, y_for_rows=136, btn_and_pad=74)

    def add_to_expression(self, value):
        if self.current_expression in ['Division by 0', 'Data error']:
            self.current_expression = ''
        self.current_expression += value
        self.update_lable()

    def number_verification(self, number):
        i = 0
        while len(number) > 1 and number[0] == '0' and number[1] != '.':
            number = number[1:]
        if len(number) > 1 and number[0] == '.':
            number = '0' + number
        return number

    def append_operator(self, operator):
        self.current_expression = self.number_verification(self.current_expression)
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_lable()
        self.update_lable()

    def update_total_lable(self):
        expression = self.total_expression
        operators = {'**': '^', '*': '\u00D7', '/': '\u00F7', '+': '+', '-': '-'}
        for operator, symbol in operators.items():
            expression = expression.replace(operator, symbol)
        self.total_lable.config(text=expression)

    def update_lable(self):
        if self.current_expression in ['Division by 0', 'Data error]:
            self.lable.config(text=self.current_expression)
        else:
            self.lable.config(text=self.current_expression[:12])

    def evaluate(self):
        self.total_expression += self.number_verification(self.current_expression)
        self.update_total_lable()
        try:
            self.current_expression = str(eval(self.total_expression))
        except ZeroDivisionError:
            self.current_expression = 'Division by 0'
        except:
            self.current_expression = 'Data error'
        finally:
            self.total_expression = ''
            self.update_lable()

    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_lable()
        self.update_total_lable()

    def run(self):
        self.initialize_interface()
        self.root.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
