from src.views.abstract_view import View
from src.entities.ball import Ball
import PySimpleGUI as sg


class BoardView(View):
    def __init__(self) -> None:
        pass

    def init_components(self) -> None:

        sg.theme("Reddit")
        layout = [
                    ['?'],
                    [sg.Submit("Change level", key='change_level', size=(20, 1), button_color='orange')],
                    [sg.Submit("Back to menu", key='back_to_menu', size=(20, 1))]
                ]

        super().__init__(sg.Window("Game Board", layout=layout, resizable=False, finalize=True, modal=True), (900, 900))

    def open(self, balls: [Ball] = None) -> str | None:
        while True:
            event, values = super().read()
            if event == 'back_to_menu' or event is None or event == sg.WIN_CLOSED:
                super().close()
                break
        return event
