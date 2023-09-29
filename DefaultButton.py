from tkinter import Button
from colors import *


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