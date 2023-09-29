from tkinter import Button
from colors import *
from enum import Enum


class ButtonTypes(Enum):
    SIGN = 1
    NUMBER = 2


class DefaultButton(Button):
    def __init__(self, target_row_frame, text, background,
                 font_style, cmd, width = 60, height = 60):
        self.__relief = 'flat'
        self.__fg = WHITE
        self.__padding = 14

        self.width = width
        self.__height = height


        super().__init__(target_row_frame, text = text, bg = background,
                         font = font_style, command = cmd,
                         relief = self.__relief, fg = self.__fg)

    def place(self, serial_number, previous_width):
        x = (self.__padding + previous_width) * serial_number
        super().place(x = x, width = self.width, height = self.__height)


class NumberButton(DefaultButton):
    def __init__(self, target_row_frame, text, cmd, width = 60, height = 60):
        self.__bg = DARK_PINK
        self.__font = ('Arial', 20)

        super().__init__(target_row_frame, text, self.__bg, self.__font, cmd)


class SignButton(DefaultButton):
    def __init__(self, target_row_frame, text, cmd, width = 60, height = 60):
        self.__bg = LIGHT_PINK
        self.__font = ('Arial', 20, 'bold')

        super().__init__(target_row_frame, text, self.__bg, self.__font, cmd, width, height)


class ButtonFactory():
    def create_button(self, target_row_frame, button_type, text, command, width = 60, height = 60):
        btn = None
        match button_type:
            case ButtonTypes.SIGN:
                btn = SignButton(target_row_frame, text, command, width, height)
            case ButtonTypes.NUMBER:
                btn = NumberButton(target_row_frame, text, command, width, height)
            case _:
                raise ValueError
        return btn
