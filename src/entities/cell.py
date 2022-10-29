from src.entities.location import Location


class Cell:
    def __init__(self, coordinates: [int], livre: bool = True) -> None:
        if isinstance(coordinates, list):
            self.__location = Location(coordinates[0], coordinates[1])
        if isinstance(livre, bool):
            self.__livre = livre

    @property
    def location(self) -> Location:
        return self.__location

    @property
    def livre(self) -> bool:
        return self.__livre

    @livre.setter
    def livre(self, livre) -> None:
        if isinstance(livre, bool):
            self.__livre = livre

    @staticmethod
    def possible_directions() -> list:
        return []
