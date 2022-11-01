import threading

from src.entities.location import Location
from src.views.abstract_view import View
from src.entities.ball import Ball
from src.entities.cell import Cell
import PySimpleGUI as sg
from src.entities.countdown_thread import CountdownThread


class BoardView(View):
    def __init__(self) -> None:
        pass

    def init_components(self) -> None:
        sg.theme("Reddit")
        layout = [
            [
                [sg.Submit('', key='0-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='0-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='1-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='1-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='2-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='2-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='3-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='3-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='4-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='4-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='5-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='5-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='6-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='6-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='7-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='7-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='8-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='8-9', size=(4, 2), button_color='white')],
                [sg.Submit('', key='9-0', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-1', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-2', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-3', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-4', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-5', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-6', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-7', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-8', size=(4, 2), button_color='white'),
                 sg.Submit('', key='9-9', size=(4, 2), button_color='white')],
            ],
            [sg.Text("   ")],
            [sg.Submit("Change level", key='change_level', size=(30, 1), button_color='orange'),
             sg.Submit("Back to menu", key='back_to_menu', size=(28, 1))],
            [sg.Text('', key='counter', justification='c')],
        ]

        super().__init__(sg.Window("Game Board", layout=layout, resizable=False, finalize=True, modal=True,
                                   element_justification='c'))

    def open(self, countdown_thread: CountdownThread, balls: [Ball], stop_thread_objects) -> str | None:
        countdown_thread.start()
        for ball in balls:
            ball.ball_thread.start()

        while True:
            event, values = super().read()

            if event == 'back_to_menu' or event is None or event == sg.WIN_CLOSED:
                stop_thread_objects()
                super().close()
                break
            if event == 'COUNT':
                count = values[event]

                if count == '1':
                    stop_thread_objects()

                    super().show_message("Time's Up", 'Game over, you lose!')
                    super().close()
                    break
                else:
                    super().window['counter'].update(value=count)
            elif '-' in event:
                if all(x.clicked for x in balls):
                    stop_thread_objects()

                    super().show_message("Victory", 'Congratulations, you won!')
                    super().close()
                    break
                for ball in balls:
                    if self.handle_click(event, ball):
                        balls.pop(balls.index(ball))

        return event

    def handle_click(self, button_key, ball):
        board_cell_location = f'{ball.cell.location.x}-{ball.cell.location.y}'

        found_ball_in_cell = board_cell_location == button_key
        if found_ball_in_cell:
            ball.stop_thread()
            ball.remove_from_board(super().window)
            return True
        return False

    def update_cell_color(self, location: Location, color):
        super().window[f'{location.x}-{location.y}'].update(button_color=color)
