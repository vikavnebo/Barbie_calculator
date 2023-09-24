from ButtonFactory import ButtonFactory


class Row():

    def __init__(self, row_number, frame):
        self.__row_number = row_number
        self.__frame = frame
        self.__buttons = []
        self.__btn_factory = ButtonFactory()

    def __place_buttons(self):
        for serial_number in range(len(self.__buttons)):
            previous_width = 0
            if serial_number > 0:
                previous_width = self.__buttons[serial_number - 1].width

            self.__buttons[serial_number].place(serial_number, previous_width)

    def place(self, pad, y_for_rows, btn_and_pad):
        self.__frame.place(
            x = pad,
            y = (y_for_rows + btn_and_pad * self.__row_number),
            height = btn_and_pad, relwidth=1
        )

        self.__place_buttons()

    def append_button(self, button_type, text, command, width = 60, height = 60):
        btn = self.__btn_factory.create_button(self.__frame, button_type, text, command, width, height)
        self.__buttons.append(btn)
