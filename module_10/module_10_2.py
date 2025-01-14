from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def fight(self, enemies=100):
        days = 0
        while enemies > 0:
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            days += 1
            print(f"{self.name} сражается {days} день(дня), осталось {enemies} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.fight()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")