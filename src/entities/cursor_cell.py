from src.entities.cell import Cell

# Célula em que está o cursor/teclado em tempo real
class CursorCell:
    def __init__(self, current_cell: Cell):
        self.__current_cell = None

        if isinstance(current_cell, Cell):
            self.__current_cell = current_cell

    @property
    def current_cell(self):
        return self.__current_cell

    @current_cell.setter
    def current_cell(self, current_cell: Cell):
        if isinstance(current_cell, Cell):
            self.__current_cell = current_cell
