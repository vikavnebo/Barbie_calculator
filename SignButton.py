from colors import *
from DefaultButton import DefaultButton


class SignButton(DefaultButton):
    def __init__(self, target_row_frame, text, cmd, width = 60, height = 60):
        self.__bg = LIGHT_PINK
        self.__font = ('Arial', 20, 'bold')

        super().__init__(target_row_frame, text, self.__bg, self.__font, cmd, width, height)
