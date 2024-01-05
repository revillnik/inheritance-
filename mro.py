class Goods:
    def __init__(self, name, price):
        super().__init__()
        self.name = self.check_name(name)
        self.price = self.check_price(price)

    def get_info(self):
        print(
            f"ID: {super().get_ID()}, Название товара: {self.name}, стоимость {self.price}"
        )

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            raise TypeError("Название товара должно быть строкой")
        return name

    @classmethod
    def check_price(cls, price):
        if type(price) not in (int, float):
            raise TypeError("Стоимость товара должна быть представлена в виде числа")
        return price


class Logs:
    id = 0

    def __init__(self):
        self.ID = Logs.id
        Logs.id += 1

    def get_ID(self):
        return self.ID


class Notebooks(Goods, Logs):
    def __init__(self, name, price):
        super().__init__(name, price)


hp = Notebooks("hp", 50000)
lenovo = Notebooks("lenovo", 40000)
hp.get_info()
lenovo.get_info()
