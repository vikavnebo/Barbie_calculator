from ButtonTypes import ButtonTypes
from SignButton import SignButton
from NumberButton import NumberButton


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
