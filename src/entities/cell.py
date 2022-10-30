from src.entities.location import Location


class Cell:
    def __init__(self, coordinates: [int], is_free: bool = True) -> None:
        if isinstance(coordinates, list):
            self.__location = Location(coordinates[0], coordinates[1])
        if isinstance(is_free, bool):
            self.__is_free = is_free

    @property
    def location(self) -> Location:
        return self.__location

    @property
    def is_free(self) -> bool:
        return self.__is_free

    @is_free.setter
    def is_free(self, is_free) -> None:
        if isinstance(is_free, bool):
            self.__is_free = is_free

    @staticmethod
    def possible_directions() -> list:
        return []
