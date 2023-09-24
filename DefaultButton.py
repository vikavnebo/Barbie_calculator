from tkinter import Button
from colors import *


class DefaultButton(Button):
    def __init__(self, target_row_frame, text, background,
                 font_style, cmd, width = 60, height = 60):
        self.__relief = 'flat'
        self.__fg = WHITE
        self.__padding = 14

        self.__width = width
        self.__height = height


        super().__init__(target_row_frame, text = text, bg = background,
                         font = font_style, command = cmd,
                         relief = self.__relief, fg = self.__fg)

    def place(self, serial_number):
        if self['text'] == 'C':
            past_width = 208
        else:
            past_width = self.__width
        x = (self.__padding + past_width) * serial_number
        super().place(x = x, width = self.__width, height = self.__height)