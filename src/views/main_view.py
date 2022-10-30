from src.views.abstract_view import View
import PySimpleGUI as sg


class MainView(View):
    def __init__(self) -> None:
        pass

    def init_components(self) -> None:
        sg.theme("Reddit")
        layout = [
                    [sg.Submit("Start Game", key='start_game', size=(20, 1))],
                    [sg.Cancel("Exit", key='cancel', size=(20, 1))]
                ]

        super().__init__(sg.Window("Threading Game", layout=layout, resizable=False, finalize=True, modal=True), (200, 100))

    def open(self) -> str | None:
        while True:
            event, values = super().read()

            if event == 'start_game':
                super().close()
                break

            if event == 'cancel' or event is None or event == sg.WIN_CLOSED:
                super().close()
                break
        return event
