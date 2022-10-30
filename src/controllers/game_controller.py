import threading
from src.controllers.thread_controller import ThreadController
from src.controllers.board_controller import BoardController
from src.views.board_view import BoardView
from src.entities.ball import Ball
from src.entities.cell import Cell
import PySimpleGUI as sg
from time import sleep


class GameController:
    def __init__(self, system_controller) -> None:
        self.__level = {}
        self.__board_view: BoardView = BoardView()
        self.__system_controller = system_controller
        self.__board = self.__create_board()

    @property
    def level(self) -> {}:
        return self.__level

    @level.setter
    def level(self, level: dict) -> None:
        if isinstance(level, dict):
            self.__level = level

    def start_game(self) -> None:
        self.__board_view.init_components()
        thread_objects = self.create_thread_objects()
        self.open_view(thread_objects, GameController.stop_thread_objects)

    def create_thread_objects(self):
        balls = [
            Ball(x) for x in BoardController.set_random_coordinates(
                self.__board, self.__board_view.update_cell_color
            )
        ]
        for ball in balls:
            ball.time_to_move = self.__level['time_to_move']
            ball.board = self.__board
            ball.ball_thread = ThreadController.create(ball.handle_ball_in_game, self.__board_view.window, 'ball')

        countdown_thread = ThreadController.create(self.handle_game_countdown, self.__board_view.window, 'countdown')

        return {'balls': balls, 'countdown': countdown_thread}

    @staticmethod
    def stop_thread_objects():
        ThreadController.stop_daemon_threads()

    def handle_game_countdown(self, window: sg.Window, inner_stop_event: threading.Event,
                              general_stop_event: threading.Event, mutex) -> None:
        countdown: int = self.__level['countdown']
        while not inner_stop_event.is_set() and not general_stop_event.is_set() and countdown:
            window['counter'].update(value=countdown)
            countdown -= 1
            sleep(1)

        self.end_game()

    def change_level(self) -> None:
        self.__board_view.close()
        self.__system_controller.start_game()

    def back_to_menu(self) -> None:
        self.__board_view.close()

    def end_game(self):
        pass

    def __create_board(self):
        board = [
            [Cell([0, 0]), Cell([0, 1]), Cell([0, 2]), Cell([0, 3]), Cell([0, 4]), Cell([0, 5]), Cell([0, 6]), Cell([0, 7]), Cell([0, 8]), Cell([0, 9])],
            [Cell([1, 0]), Cell([1, 1]), Cell([1, 2]), Cell([1, 3]), Cell([1, 4]), Cell([1, 5]), Cell([1, 6]), Cell([1, 7]), Cell([1, 8]), Cell([1, 9])],
            [Cell([2, 0]), Cell([2, 1]), Cell([2, 2]), Cell([2, 3]), Cell([2, 4]), Cell([2, 5]), Cell([2, 6]), Cell([2, 7]), Cell([2, 8]), Cell([2, 9])],
            [Cell([3, 0]), Cell([3, 1]), Cell([3, 2]), Cell([3, 3]), Cell([3, 4]), Cell([3, 5]), Cell([3, 6]), Cell([3, 7]), Cell([3, 8]), Cell([3, 9])],
            [Cell([4, 0]), Cell([4, 1]), Cell([4, 2]), Cell([4, 3]), Cell([4, 4]), Cell([4, 5]), Cell([4, 6]), Cell([4, 7]), Cell([4, 8]), Cell([4, 9])],
            [Cell([5, 0]), Cell([5, 1]), Cell([5, 2]), Cell([5, 3]), Cell([5, 4]), Cell([5, 5]), Cell([5, 6]), Cell([5, 7]), Cell([5, 8]), Cell([5, 9])],
            [Cell([6, 0]), Cell([6, 1]), Cell([6, 2]), Cell([6, 3]), Cell([6, 4]), Cell([6, 5]), Cell([6, 6]), Cell([6, 7]), Cell([6, 8]), Cell([6, 9])],
            [Cell([7, 0]), Cell([7, 1]), Cell([7, 2]), Cell([7, 3]), Cell([7, 4]), Cell([7, 5]), Cell([7, 6]), Cell([7, 7]), Cell([7, 8]), Cell([7, 9])],
            [Cell([8, 0]), Cell([8, 1]), Cell([8, 2]), Cell([8, 3]), Cell([8, 4]), Cell([8, 5]), Cell([8, 6]), Cell([8, 7]), Cell([8, 8]), Cell([8, 9])],
            [Cell([9, 0]), Cell([9, 1]), Cell([9, 2]), Cell([9, 3]), Cell([9, 4]), Cell([9, 5]), Cell([9, 6]), Cell([9, 7]), Cell([9, 8]), Cell([9, 9])],
        ]
        return board

    def open_view(self, thread_objects: dict, stop_thread_objects) -> None:
        options = {
            'change_level': self.change_level,
            'back_to_menu': self.back_to_menu
        }

        while True:
            option = self.__board_view.open(thread_objects['countdown'], thread_objects['balls'], stop_thread_objects)

            if option is None or sg.WIN_CLOSED:
                self.back_to_menu()
                break

            options[option]()


"""
thread = threading.Thread(target=function, args=(arg1,), daemon=True).start()

"""
