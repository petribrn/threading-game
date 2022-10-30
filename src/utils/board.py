from src.entities.cell import Cell

__board = [
    [Cell([0, 0]), Cell([0, 1]), Cell([0, 2]), Cell([0, 3]), Cell([0, 4]), Cell([0, 5]), Cell([0, 6]), Cell([0, 7]), Cell([0, 8]), Cell([0, 9])],
    [Cell([1, 0]), Cell([1, 1]), Cell([1, 2]), Cell([1, 3]), Cell([1, 4]), Cell([1, 5]), Cell([1, 6]), Cell([1, 7]), Cell([1, 8]), Cell([1, 9])],
    [Cell([2, 0]), Cell([2, 1]), Cell([2, 2]), Cell([2, 3]), Cell([2, 4]), Cell([2, 5]), Cell([2, 6]), Cell([2, 7]), Cell([2, 8]), Cell([2, 9])],
    [Cell([3, 0]), Cell([3, 1]), Cell([3, 2]), Cell([3, 3]), Cell([3, 4]), Cell([3, 5]), Cell([3, 6]), Cell([3, 7]), Cell([3, 8]), Cell([3, 9])],
    [Cell([4, 0]), Cell([4, 1]), Cell([4, 2]), Cell([4, 3]), Cell([4, 4]), Cell([4, 5]), Cell([4, 6]), Cell([4, 7]), Cell([4, 8]), Cell([4, 9])],
    [Cell([5, 0]), Cell([5, 1]), Cell([5, 2]), Cell([5, 3]), Cell([5, 4]), Cell([5, 5]), Cell([5, 6]), Cell([5, 7]), Cell([5, 8]), Cell([5, 9])],
    [Cell([6, 0]), Cell([6, 1]), Cell([6, 2]), Cell([6, 3]), Cell([6, 4]), Cell([6, 5]), Cell([6, 6]), Cell([6, 7]), Cell([6, 8]), Cell([6, 9])],
    [Cell([7, 0]), Cell([7, 1]), Cell([7, 2]), Cell([7, 3]), Cell([7, 4]), Cell([7, 5]), Cell([7, 6]), Cell([7, 7]), Cell([7, 8]), Cell([7, 9])],
    [Cell([8, 0]), Cell([8, 1]), Cell([8, 2]), Cell([8, 3]), Cell([8, 4]), Cell([8, 5]), Cell([8, 6]), Cell([8, 7]), Cell([8, 8]), Cell([8, 9])],
    [Cell([9, 0]), Cell([9, 1]), Cell([9, 2]), Cell([9, 3]), Cell([9, 4]), Cell([9, 5]), Cell([9, 6]), Cell([9, 7]), Cell([9, 8]), Cell([9, 9])],
]


def cell(coordinates: [int]) -> Cell:
    # 0: x, 1: y
    cell_instance: Cell = __board[coordinates[0]][coordinates[1]]
    return cell_instance


def set_filled_cell(coordinates: [int], update_view_function) -> None:
    cell_instance: Cell = __board[coordinates[0]][coordinates[1]]

    cell_instance.is_free = False
    update_view_function(cell_instance)


def set_free_cell(coordinates: [int], update_view_function) -> None:
    cell_instance: Cell = __board[coordinates[0]][coordinates[1]]

    cell_instance.is_free = True
    update_view_function(cell_instance)
