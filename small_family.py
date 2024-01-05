class Animals:
    def give_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


class Cats(Animals):
    def __init__(self):
        print(
            'Вы завели кошку, как хотите её назвать? (впишите имя через команду x.give_name("имя")'
        )


class Dogs(Animals):
    def __init__(self):
        print(
            'Вы завели собаку, как хотите её назвать? Впишите имя через команду x.give_name("имя")'
        )


vas = Cats()
vas.give_name("Пуська")
vas.get_name()
print(isinstance(vas, Animals))
