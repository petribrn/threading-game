from src.entities.cell import Cell


class Ball:
    def __init__(self, cell: Cell) -> None:
        self.__cell: Cell | None = None
        self.__clicked: bool = False
        if isinstance(cell, Cell) and cell.livre:
            self.__cell = cell

    @property
    def cell(self) -> Cell:
        return self.__cell

    def update_current_cell(self, cell: Cell) -> None:
        if isinstance(cell, Cell) and cell.livre:
            self.__cell = cell

    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, clicked: bool):
        if isinstance(clicked, bool):
            self.__clicked = clicked
