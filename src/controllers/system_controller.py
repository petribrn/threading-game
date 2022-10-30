from src.views.main_view import MainView
from src.views.levels_view import LevelsView
from src.controllers.game_controller import GameController
import PySimpleGUI as sg


class SystemController:
    def __init__(self):
        self.__main_view = MainView()
        self.__levels_view = LevelsView()
        self.__controllers = {}

    def init_system(self):
        self.init_controllers()
        self.open_view()

    def init_controllers(self):
        self.__controllers['game_controller']: GameController = GameController(self)

    def start_game(self):
        self.__levels_view.init_components()
        print('levels')
        chosen_level = self.__levels_view.open()

        self.__controllers['game_controller'].level = chosen_level
        self.__controllers['game_controller'].start_game()

    @staticmethod
    def exit_game():
        exit(0)

    def open_view(self):
        options = {
            'start_game': self.start_game,
            'cancel': self.exit_game,
        }

        while True:
            self.__main_view.init_components()
            option = self.__main_view.open()
            self.__main_view.close()
            if option is None or sg.WIN_CLOSED:
                SystemController.exit_game()
                break

            options[option]()
