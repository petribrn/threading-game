import random
from src.entities.cell import Cell
from src.utils.board import cell
from src.views.board_view import BoardView
import PySimpleGUI as sg
from src.controllers.system_controller import SystemController
from src.entities.ball import Ball
import time


class BoardController:
    def __init__(self, system_controller: SystemController) -> None:
        self.__level = dict | None
        self.__time = int | None
        self.__board_view: BoardView = BoardView()
        self.__system_controller: SystemController = system_controller

    @property
    def level(self):
        return self.__level

    @property
    def time(self):
        return self.__time

    @level.setter
    def level(self, level: dict):
        if isinstance(level, dict):
            self.__level = level

    def start_game(self):
        balls = [Ball(BoardController.random_coordinates())] * 5
        self.open_view(balls)

    def change_level(self):
        self.__board_view.close()
        self.__system_controller.start_game()

    @staticmethod
    def random_coordinates() -> Cell:
        random_x = random.randrange(0, 9)
        random_y = random.randrange(0, 9)

        return cell([random_x, random_y])

    def back_to_menu(self):
        self.__board_view.close()

    def open_view(self, balls: [Ball]):
        options = {
            'change_level': self.change_level,
            'back_to_menu': self.back_to_menu
        }

        while True:
            self.__board_view.init_components()
            option = self.__board_view.open()

            if option is None or sg.WIN_CLOSED:
                self.back_to_menu()
                break

            options[option]()
