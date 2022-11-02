import PySimpleGUI as sg

from src.views.board_view import BoardView


class GameController:
    def __init__(self, system_controller, board_view) -> None:
        self.__board_view: BoardView = board_view
        self.__system_controller = system_controller

    def start_game(self, thread_objects: dict, stop_thread_objects) -> None:
        self.open_view(thread_objects, stop_thread_objects)

    @staticmethod
    def end_game():
        exit(0)

    def open_view(self, thread_objects: dict, stop_thread_objects) -> None:

        while True:
            option = self.__board_view.open(thread_objects['countdown'], thread_objects['balls'], stop_thread_objects)

            if option in ('victory', 'defeat', 'exit', '-') or option is None or sg.WIN_CLOSED:
                GameController.end_game()
                break
