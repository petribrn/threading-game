import threading
from src.controllers.thread_controller import ThreadController
from src.controllers.board_controller import BoardController
from src.entities.location import Location
from src.views.board_view import BoardView
from src.entities.ball import Ball
from src.entities.board import Board
import PySimpleGUI as sg
from time import sleep


class GameController:
    def __init__(self, system_controller) -> None:
        self.__level = {}
        self.__board_view: BoardView = BoardView()
        self.__system_controller = system_controller

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
                Board.game_board, self.__board_view.update_cell_color
            )
        ]
        for ball in balls:
            ball.time_to_move = self.__level['time_to_move']
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
            if inner_stop_event.is_set() or general_stop_event.is_set():
                break
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
        exit(0)


    def open_view(self, thread_objects: dict, stop_thread_objects) -> None:
        options = {
            'change_level': self.change_level,
            'back_to_menu': self.back_to_menu
        }

        while True:
            option = self.__board_view.open(thread_objects['countdown'], thread_objects['balls'], stop_thread_objects)

            if option in ('victory', 'defeat'):
                self.back_to_menu()
                break
            if option is None or sg.WIN_CLOSED:
                self.back_to_menu()
                break

            if '-' in option:
                option = 'back_to_menu'

            options[option]()


"""
thread = threading.Thread(target=function, args=(arg1,), daemon=True).start()

"""
