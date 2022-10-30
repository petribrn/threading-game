import random

from src.entities.cell import Cell
from src.entities.location import Location


class BoardController:

    @staticmethod
    def board_cell(board: [], location: Location) -> Cell:
        cell_instance: Cell = board[location.x][location.y]
        return cell_instance

    @staticmethod
    def set_cell_state(board: [], update_view_function, location: Location, color: str = 'white') -> None:
        cell_instance: Cell = board[location.x][location.y]

        if color == 'white':
            cell_instance.is_free = True
        else:
            cell_instance.is_free = False

        update_view_function(location, color)

    @staticmethod
    def set_random_coordinates(board: [], update_view_function) -> [Cell]:
        balls_locations = []

        while len(balls_locations) < 5:
            new_cell = BoardController.get_new_cell_coordinates(board)
            print(new_cell.is_free)
            if new_cell.is_free:
                balls_locations.append(new_cell.location)
                BoardController.set_cell_state(board, update_view_function, new_cell.location, 'green')

        cells_list = [BoardController.board_cell(board, bl) for bl in balls_locations]
        print(cells_list)
        return cells_list

    @staticmethod
    def get_new_cell_coordinates(board: []):
        new_location = Location(random.randrange(0, 9), random.randrange(0, 9))

        return BoardController.board_cell(board, new_location)
