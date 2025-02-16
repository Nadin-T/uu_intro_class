class House():

    houses_history = []

    def __new__(cls, *args, **kwargs): #добавление дома в историю
        house = args[0]
        cls.houses_history.append(house)
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует.')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): #меньше, чем
        return self.number_of_floors < other.number_of_floors

    def  __le__(self, other): #меньше или равно
        return self.number_of_floors <= other.number_of_floors

    def  __gt__(self, other): #больше, чем
        return self.number_of_floors > other.number_of_floors

    def  __ge__(self, other): #больше или равно
        return self.number_of_floors >= other.number_of_floors

    def  __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value): #чем отличается от iadd?
        self.number_of_floors += value
        return self

    def __radd__(self, value): #+ объект справа
        return self.__add__(value)

    def __iadd__(self, value): # += перезаписывает
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')

if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2) # __eq__

    h1 = h1 + 10 # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10 # __iadd__
    print(h1)

    h2 = 10 + h2 # __radd__
    print(h2)

    print(h1 > h2) # __gt__
    print(h1 >= h2) # __ge__
    print(h1 < h2) # __lt__
    print(h1 <= h2) # __le__
    print(h1 != h2) # __ne__