import threading
from src.controllers.thread_controller import ThreadController
from src.entities.location import Location
from src.views.board_view import BoardView
from src.entities.ball import Ball
from src.entities.board import Board
import PySimpleGUI as sg
from time import sleep


class GameController:
    def __init__(self, system_controller, board_view) -> None:
        self.__board_view: BoardView = board_view
        self.__system_controller = system_controller

    def start_game(self, thread_objects: dict, stop_thread_objects) -> None:
        #self.__board_view.init_components()
        self.open_view(thread_objects, stop_thread_objects)

    def change_level(self) -> None:
        self.__board_view.close()
        self.__system_controller.init_game()

    def back_to_menu(self) -> None:
        self.__board_view.close()

    def open_view(self, thread_objects: dict, stop_thread_objects) -> None:
        options = {
            'change_level': self.change_level,
            'back_to_menu': self.back_to_menu
        }

        while True:
            option = self.__board_view.open(thread_objects['countdown'], thread_objects['balls'], stop_thread_objects)

            if option in ('victory', 'defeat', 'back_to_menu'):
                self.back_to_menu()
                break
            if option is None or sg.WIN_CLOSED:
                self.back_to_menu()
                break

            if '-' in option:
                option = 'back_to_menu'

            options[option]()
