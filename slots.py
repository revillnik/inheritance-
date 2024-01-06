import timeit


class Point2D:
    __slots__ = ("x", "y")
    max_coord = 100
    min_coord = 0

    def __init__(self, x, y):
        if self.__check_coord(x, y):
            self.x = x
            self.y = y
        else:
            raise TypeError("Координаты - целые числа от 0 до 100")

    @classmethod
    def __check_coord(cls, *args):
        z = list(args)
        k = [type(i) == int and cls.min_coord <= i <= cls.max_coord for i in args]
        if not all(k):
            return False
        else:
            return True

    def calc(self):
        self.x + self.y
        del self.y
        self.y = 0


class Pointall:
    max_coord = 100
    min_coord = 0

    def __init__(self, x, y):
        if self.__check_coord(x, y):
            self.x = x
            self.y = y
        else:
            raise TypeError("Координаты - целые числа от 0 до 100")

    @classmethod
    def __check_coord(cls, *args):
        z = list(args)
        k = [type(i) == int and cls.min_coord <= i <= cls.max_coord for i in args]
        if not all(k):
            return False
        else:
            return True

    def calc(self):
        self.x + self.y
        del self.y
        self.y = 0


a = Point2D(10, 100)
b = Pointall(10, 100)

ta = timeit.timeit(a.calc)
tb = timeit.timeit(b.calc)
print(ta, tb)

print(a.__sizeof__())
print(b.__sizeof__() + b.__dict__.__sizeof__())
