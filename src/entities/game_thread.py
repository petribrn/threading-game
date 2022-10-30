import threading
import PySimpleGUI as sg
from abc import ABC, abstractmethod


class GameThread(ABC):
    @abstractmethod
    def __init__(self, target_function, general_stop_event: threading.Event, window: sg.Window, mutex: threading.Lock):
        self.__inner_stop_event = threading.Event()
        self.__general_stop_event = general_stop_event
        self.__mutex = mutex
        self.__window = window
        self.__target_function = target_function
        self._thread_instance: threading.Thread = self.create_thread_instance()

    @property
    def thread_instance(self) -> threading.Thread:
        return self._thread_instance

    def create_thread_instance(self):
        return threading.Thread(target=self.__target_function,
                                args=(self.__window, self.__inner_stop_event,
                                      self.__general_stop_event, self.__mutex), daemon=True)

    def stop(self) -> None:
        self.__inner_stop_event.set()

    def start(self) -> None:
        self._thread_instance.start()
