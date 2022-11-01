from src.entities.cell import Cell
import random
from src.entities.location import Location


class Board:
    game_board = [
        [Cell([0, 0]), Cell([0, 1]), Cell([0, 2]), Cell([0, 3]), Cell([0, 4]), Cell([0, 5]), Cell([0, 6]),
         Cell([0, 7]), Cell([0, 8]), Cell([0, 9])],
        [Cell([1, 0]), Cell([1, 1]), Cell([1, 2]), Cell([1, 3]), Cell([1, 4]), Cell([1, 5]), Cell([1, 6]),
         Cell([1, 7]), Cell([1, 8]), Cell([1, 9])],
        [Cell([2, 0]), Cell([2, 1]), Cell([2, 2]), Cell([2, 3]), Cell([2, 4]), Cell([2, 5]), Cell([2, 6]),
         Cell([2, 7]), Cell([2, 8]), Cell([2, 9])],
        [Cell([3, 0]), Cell([3, 1]), Cell([3, 2]), Cell([3, 3]), Cell([3, 4]), Cell([3, 5]), Cell([3, 6]),
         Cell([3, 7]), Cell([3, 8]), Cell([3, 9])],
        [Cell([4, 0]), Cell([4, 1]), Cell([4, 2]), Cell([4, 3]), Cell([4, 4]), Cell([4, 5]), Cell([4, 6]),
         Cell([4, 7]), Cell([4, 8]), Cell([4, 9])],
        [Cell([5, 0]), Cell([5, 1]), Cell([5, 2]), Cell([5, 3]), Cell([5, 4]), Cell([5, 5]), Cell([5, 6]),
         Cell([5, 7]), Cell([5, 8]), Cell([5, 9])],
        [Cell([6, 0]), Cell([6, 1]), Cell([6, 2]), Cell([6, 3]), Cell([6, 4]), Cell([6, 5]), Cell([6, 6]),
         Cell([6, 7]), Cell([6, 8]), Cell([6, 9])],
        [Cell([7, 0]), Cell([7, 1]), Cell([7, 2]), Cell([7, 3]), Cell([7, 4]), Cell([7, 5]), Cell([7, 6]),
         Cell([7, 7]), Cell([7, 8]), Cell([7, 9])],
        [Cell([8, 0]), Cell([8, 1]), Cell([8, 2]), Cell([8, 3]), Cell([8, 4]), Cell([8, 5]), Cell([8, 6]),
         Cell([8, 7]), Cell([8, 8]), Cell([8, 9])],
        [Cell([9, 0]), Cell([9, 1]), Cell([9, 2]), Cell([9, 3]), Cell([9, 4]), Cell([9, 5]), Cell([9, 6]),
         Cell([9, 7]), Cell([9, 8]), Cell([9, 9])],
    ]

    @classmethod
    def get_board(cls):
        return Board.game_board

    @classmethod
    def update_board_cell_state(cls, location, is_free):
        Board.game_board[location.x][location.y].is_free = is_free

    @classmethod
    def board_cell(cls, location: Location) -> Cell:
        cell_instance: Cell = Board.game_board[location.x][location.y]
        return cell_instance

    @classmethod
    def set_cell_state(cls, update_view_function, location: Location, color: str = 'white') -> None:
        cell_instance: Cell = Board.game_board[location.x][location.y]

        if color == 'white':
            cell_instance.is_free = True
        else:
            cell_instance.is_free = False

        update_view_function(location, color)

    @classmethod
    def set_random_coordinates(cls, update_view_function) -> [Cell]:
        balls_locations = []

        while len(balls_locations) < 5:
            new_cell = Board.get_new_cell_coordinates()
            if new_cell.is_free:
                balls_locations.append(new_cell.location)
                Board.set_cell_state(update_view_function, new_cell.location, 'green')

        cells_list = [Board.board_cell(bl) for bl in balls_locations]
        return cells_list

    @classmethod
    def get_new_cell_coordinates(cls):
        new_location = Location(random.randrange(0, 9), random.randrange(0, 9))

        return Board.board_cell(new_location)

