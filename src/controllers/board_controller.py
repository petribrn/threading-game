import random
import threading
from src.controllers.thread_handler_controller import ThreadHandlerController
from src.entities.cell import Cell
from src.utils.board import cell, set_filled_cell
from src.views.board_view import BoardView
from src.entities.ball import Ball
import PySimpleGUI as sg
from time import sleep


class BoardController:
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
        # countdown: int = self.__level['countdown']
        # time_to_move: float = self.__level['time_to_move']

        balls = [Ball(x) for x in self.random_coordinates()]
        functions = {
            'handle_countdown': self.handle_countdown,
        }

        countdown_thread = ThreadHandlerController.create(functions['handle_countdown'], self.__board_view.window)
        self.open_view(countdown_thread, balls)

        # while countdown > 0:
        #     balls = [Ball(x) for x in self.random_coordinates()]
        #     countdown -= time_to_move

    def handle_countdown(self, window: sg.Window, stop_event: threading.Event):
        countdown: int = self.__level['countdown']
        while not stop_event.is_set() and countdown:
            window['counter'].update(value=countdown)
            countdown -= 1
            sleep(1)

        self.end_game()

    def change_level(self) -> None:
        self.__board_view.close()
        self.__system_controller.start_game()

    def random_coordinates(self) -> [Cell]:
        balls_coordinates = []

        while len(balls_coordinates) < 5:
            new_coordinate = [random.randrange(0, 9), random.randrange(0, 9)]
            if cell(new_coordinate).is_free:
                balls_coordinates.append(new_coordinate)
                set_filled_cell(new_coordinate, self.__board_view.update_cell_green)

        cells_list = [cell(x) for x in balls_coordinates]
        return cells_list

    def back_to_menu(self) -> None:
        self.__board_view.close()

    def end_game(self):
        pass

    def open_view(self, functions, balls: [Ball]) -> None:
        options = {
            'change_level': self.change_level,
            'back_to_menu': self.back_to_menu
        }

        while True:
            self.__board_view.init_components()
            option = self.__board_view.open(functions, balls)

            if option is None or sg.WIN_CLOSED:
                self.back_to_menu()
                break

            options[option]()


"""
thread = threading.Thread(target=function, args=(arg1,), daemon=True).start()

"""