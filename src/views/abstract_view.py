from abc import ABC, abstractmethod
import PySimpleGUI as sg


class View(ABC):
    @abstractmethod
    def __init__(self, window, dimension=None):
        self.__window = window
        if dimension is not None:
            self.__window.set_min_size(dimension)

    @abstractmethod
    def init_components(self):
        pass

    @abstractmethod
    def open(self):
        pass

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, msg):
        sg.Popup(titulo, msg)

    def read(self):
        botao, valores = self.__window.read()
        return botao, valores

    def update(self, key: str, value):
        self.__window[key].update(value)

    def view_options(self):
        return self.open()
