import threading

from src.views.main_view import MainView
from src.views.levels_view import LevelsView
from src.controllers.game_controller import GameController
import PySimpleGUI as sg
from src.entities.ball import Ball
from src.entities.board import Board
from src.views.board_view import BoardView
from src.controllers.thread_controller import ThreadController
from time import sleep


class SystemController:
    def __init__(self):
        self.__main_view = MainView()
        self.__levels_view = LevelsView()
        self.__board_view: BoardView = BoardView()
        self.__game_level = None
        self.__controllers = {}

    def init_system(self):
        self.init_controllers()
        self.open_view()

    def init_controllers(self):
        self.__controllers['game_controller']: GameController = GameController(self, self.__board_view)

    def init_game(self):
        self.choose_level()

        thread_objects = self.create_thread_objects()

        self.__controllers['game_controller'].start_game(thread_objects, ThreadController.stop_daemon_threads)

    def choose_level(self):
        while True:
            self.__levels_view.init_components()
            chosen_level = self.__levels_view.open()
            if chosen_level in ('cancel', None, sg.WIN_CLOSED):
                self.__levels_view.close()
                break
            self.__game_level = chosen_level
            return

        self.open_view()

    def create_thread_objects(self):
        self.__board_view.init_components()
        balls = []
        for i in range(5):
            ball = Ball(Board.set_ball_random_coordinates())
            self.__board_view.update_cell_color_filled(ball.cell.location)

            ball.time_to_move = self.__game_level['time_to_move']
            ball.ball_thread = ThreadController.create(ball.handle_ball_in_game,
                                                       self.__board_view.window, 'ball')
            balls.append(ball)

        countdown_thread = ThreadController.create(self.handle_game_countdown, self.__board_view.window,
                                                   'countdown')

        return {'balls': balls, 'countdown': countdown_thread}

    def handle_game_countdown(self, window: sg.Window, inner_stop_event: threading.Event,
                              general_stop_event: threading.Event, mutex) -> None:
        countdown: int = self.__game_level['countdown']
        while not inner_stop_event.is_set() and not general_stop_event.is_set() and countdown:
            if inner_stop_event.is_set() or general_stop_event.is_set():
                break
            window['counter'].update(value=countdown)
            countdown -= 1

            sleep(1)

        # Counter is 0
        window['counter'].update(value=countdown)
        # Send event end_game
        window.write_event_value('TIME_UP', True)

    @staticmethod
    def exit_game():
        exit(0)

    def open_view(self):
        options = {
            'start_game': self.init_game,
            'cancel': SystemController.exit_game,
        }

        while True:
            self.__main_view.init_components()
            option = self.__main_view.open()
            self.__main_view.close()

            if option is None or sg.WIN_CLOSED:
                SystemController.exit_game()
                break

            options[option]()
