from src.entities.ball_thread import BallThread
from src.entities.board import Board
from src.entities.cell import Cell
import threading
import PySimpleGUI as sg
from time import sleep
from src.controllers.board_controller import BoardController
from src.controllers.game_controller import GameController


class Ball:
    def __init__(self, cell: Cell) -> None:
        self.__cell: Cell | None = None
        self.__clicked: bool = False

        if isinstance(cell, Cell):
            self.__cell = cell
        self.__time_to_move = None
        self.__board = None
        self.__ball_thread: BallThread | None = None

    @property
    def cell(self) -> Cell:
        return self.__cell

    def update_current_cell(self, cell: Cell) -> None:
        if isinstance(cell, Cell) and cell.is_free:
            self.__cell = cell

    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, clicked: bool):
        if isinstance(clicked, bool):
            self.__clicked = clicked

    @property
    def time_to_move(self):
        return self.__time_to_move

    @time_to_move.setter
    def time_to_move(self, time_to_move: float | int):
        if isinstance(time_to_move, float) or isinstance(time_to_move, int):
            self.__time_to_move = time_to_move

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board: list):
        if isinstance(board, list):
            self.__board = board

    @property
    def ball_thread(self):
        return self.__ball_thread

    @ball_thread.setter
    def ball_thread(self, ball_thread: BallThread):
        if isinstance(ball_thread, BallThread):
            self.__ball_thread = ball_thread

    def stop_thread(self):
        self.__ball_thread.stop()

    def handle_ball_in_game(self, window: sg.Window, inner_stop_event: threading.Event,
                            general_stop_event: threading.Event, mutex: threading.Lock):
        while not inner_stop_event.is_set() and not general_stop_event.is_set():
            sleep(self.__time_to_move)
            self.set_random_coordinates(window, self.__board, mutex)

        return

    def set_random_coordinates(self, window: sg.Window, board, mutex) -> [Cell]:
        new_cell = BoardController.get_new_cell_coordinates(board)

        if new_cell.is_free:
            mutex.acquire()
            self.remove_from_board(window)

            self.__cell = new_cell
            self.update_location_in_board(window)
            mutex.release()
            return
        else:
            self.set_random_coordinates(window, board, mutex)

    def update_location_in_board(self, window: sg.Window):
        window[f'{self.__cell.location.x}-{self.__cell.location.y}'].update(button_color='green')
        Board.update_board_cell_state(self.__cell.location, True)

    def remove_from_board(self, window: sg.Window):
        self.__cell.is_free = True

        window[f'{self.__cell.location.x}-{self.__cell.location.y}'].update(button_color='white')
        Board.update_board_cell_state(self.__cell.location, True)
