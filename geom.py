class Geom:
    def __init__(self, x, y):
        if self.__check_coord(x, y):
            self.__x = x
            self.__y = y
        else:
            print("Координатами могут быть только целые числа")

    @classmethod
    def __check_coord(cls, *args):
        z = list(args)
        k = [type(i) == int for i in args]
        if not all(k):
            return False
        else:
            return True
    def get_coords(self):
            print((self.__x, self.__y))


class React(Geom):
    def __init__(self, x, y, fill="No"):
        super().__init__(x, y)
        self.check_fill(fill)
        self.fill = fill
        print("Вы создали квадрат")

    @classmethod
    def check_fill(cls, fill):
        if type(fill) != str:
            raise TypeError("Наличие заливки пишется буквами")


a = React(0, 1, "Yes")
print(a.__dict__)
a.get_coords()
