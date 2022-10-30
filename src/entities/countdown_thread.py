import threading
from src.entities.game_thread import GameThread
import PySimpleGUI as sg


class CountdownThread(GameThread):
    def __init__(self, target_function, general_stop_event: threading.Event, window: sg.Window, mutex: threading.Lock):
        super().__init__(target_function, general_stop_event, window, mutex)

