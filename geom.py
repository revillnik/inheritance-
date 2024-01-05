class Geom:
    name = 'Geom'
    def __init__(self, x, y):
        if self.__check_coord(x, y):
            self.x = x
            self.y = y
        else:
            print("Координатами могут быть только целые числа")
    def get_perimetre(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод get_perimetre()")

    @classmethod
    def __check_coord(cls, *args):
        z = list(args)
        k = [type(i) == int for i in args]
        if not all(k):
            return False
        else:
            return True

    def get_coords(self):
        print((self.x, self.y))


class React(Geom):
    def __init__(self, x, y, fill="No"):
        super().__init__(x, y)
        self.check_fill(fill)
        self.fill = fill
        self.name = "Квадрат"
        print("Вы создали квадрат")

    def get_perimetre(self):
        return self.x * self.y

    @classmethod
    def check_fill(cls, fill):
        if type(fill) != str:
            raise TypeError("Наличие заливки пишется буквами")


class Cube(Geom):
    def __init__(self, x):
        y = x
        super().__init__(x, y)
        self.name = "Куб"
        print("Вы создали куб")

    def get_perimetre(self):
        return self.x**2


a = React(0, 1, "Yes")
print(a.__dict__)
a.get_coords()
figures = (Cube(5), React(2, 3))
k = 0
for i in figures:
    k += 1
    print(f"Периметр равен фигуры {i.name}:", i.get_perimetre())
