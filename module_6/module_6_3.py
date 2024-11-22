"""
Множественное наследование
"""
import random
class Animal:
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
        return self._cords

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}.')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        return


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Here are(is) {eggs_count} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        if dz < 0:
           dz = abs(dz)
        self._cords[2] -= dz * (self.speed / 2)
        return self._cords

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

if __name__ == '__main__':
    print(Duckbill.mro())
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()

