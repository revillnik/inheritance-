class Geom:
    def __init__(self, x, y):
          if self.check_coord(x,y):
                 self.x = x
                 self.y = y
          else:
               print('Координатами могут быть только целые числа')
    @classmethod
    def check_coord(cls, *args):
        z = list(args)
        k = [type(i) == int for i in args]
        if not all(k):
            return False
        else:
            return True

class React(Geom):
     def __init__(self, x,y, fill='No'):
          super().__init__(x,y)
          self.check_fill(fill)
          self.fill = fill 
          print('Вы создали квадрат')
     @classmethod
     def check_fill(cls, fill):
          if type(fill) != str:
                raise TypeError('Наличие заливки пишется буквами')

a = React(0, 1, 'Yes')
print(a.__dict__)