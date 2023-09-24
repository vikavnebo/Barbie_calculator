from tkinter import Tk, Frame, Button, Label, messagebox

from colors import *
from ButtonFactory import *
from Row import *
from Calculate_Utils import *


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('310x506')
        self.root.resizable(0, 0)
        self.root.title('Barbie Calculator')
        self.root.iconbitmap('calc.ico')

        self.main_frame = self.create_main_frame()
        self.result_frame = self.create_result_frame()

        self.result_lable = self.create_result_lable()
        self.result_lable = self.create_history()

    def create_main_frame(self):
        frame = Frame(self.root, bg=WHITE)
        frame.place(relwidth=1, relheight=1)
        return frame

    def create_result_frame(self):
        frame = Frame(self.root, bg=LIGHT_PINK, height=122)
        frame.place(relwidth=1, height=122)
        # frame.pack(expand=True, fill='both')
        return frame

    def create_result_lable(self):
        lable = Label(self.result_frame, text='0', bg=LIGHT_PINK,
                      fg=WHITE, font=('Arial', 32, 'bold'))
        lable.place(x=25, y=61)
        return lable

    def create_history(self):
        lable = Label(self.result_frame, text='', bg=LIGHT_PINK,
                        fg=WHITE, font=('Arial', 16))
        lable.place(x=25, y=25)
        return lable

    def initialize_interface(self):
        rows = []
        for row_number in range(5):
            rows.append(Row(row_number, Frame(self.main_frame, bg=WHITE)))

        rows[0].append_button(ButtonTypes.SIGN, '=', lambda x: True, width = 208)
        rows[0].append_button(ButtonTypes.SIGN, 'C', lambda x: True)

        rows[1].append_button(ButtonTypes.NUMBER, '1', lambda x: True)
        rows[1].append_button(ButtonTypes.NUMBER, '2', lambda x: True)
        rows[1].append_button(ButtonTypes.NUMBER, '3', lambda x: True)
        rows[1].append_button(ButtonTypes.SIGN, '+', lambda x: True)

        rows[2].append_button(ButtonTypes.NUMBER, '4', lambda x: True)
        rows[2].append_button(ButtonTypes.NUMBER, '5', lambda x: True)
        rows[2].append_button(ButtonTypes.NUMBER, '6', lambda x: True)
        rows[2].append_button(ButtonTypes.SIGN, '-', lambda x: True)

        rows[3].append_button(ButtonTypes.NUMBER, '7', lambda x: True)
        rows[3].append_button(ButtonTypes.NUMBER, '8', lambda x: True)
        rows[3].append_button(ButtonTypes.NUMBER, '9', lambda x: True)
        rows[3].append_button(ButtonTypes.SIGN, 'x', lambda x: True)

        rows[4].append_button(ButtonTypes.SIGN, '^', lambda x: True)
        rows[4].append_button(ButtonTypes.NUMBER, '0', lambda x: True)
        rows[4].append_button(ButtonTypes.SIGN, '√', lambda x: True)
        rows[4].append_button(ButtonTypes.SIGN, '/', lambda x: True)

        for row in rows:
            row.place(pad=14, y_for_rows=136, btn_and_pad=74)

    def run(self):
        self.initialize_interface()
        self.root.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()
