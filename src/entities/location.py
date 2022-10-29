class Location:
    def __init__(self, x: int, y: int) -> None:
        self.__x = None
        self.__y = None

        if isinstance(x, int):
            self.__x = x
        if isinstance(y, int):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        if isinstance(x, int):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        if isinstance(y, int):
            self.__y = y
