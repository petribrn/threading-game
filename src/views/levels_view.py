from src.views.abstract_view import View
import PySimpleGUI as sg
from src.enums.enums import GameModeEnum


class LevelsView(View):
    def __init__(self) -> None:
        pass

    def init_components(self) -> None:
        sg.theme("Reddit")
        layout = [
                    [sg.Submit("Easy", key='easy', size=(20, 1), button_color='green')],
                    [sg.Submit("Medium", key='medium', size=(20, 1), button_color='orange')],
                    [sg.Submit("Hardcore", key='hardcore', size=(20, 1), button_color='red')],
                    [sg.Submit("Cancel", key='cancel', size=(20, 1), button_color='red')]
                ]

        super().__init__(sg.Window("Select Level", layout=layout, resizable=False, finalize=True, modal=True), (200, 300))

    def open(self) -> {} | None:
        while True:
            event, values = super().read()

            if event == 'cancel' or event is None or event == sg.WIN_CLOSED:
                return super().close()
            if event == 'easy':
                return GameModeEnum.easy.value
            elif event == 'medium':
                return GameModeEnum.medium.value
            elif event == 'hardcore':
                return GameModeEnum.hardcore.value
