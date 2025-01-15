import threading
from random import randint
from time import sleep


class Bank:
    """Конструктор класса Банк"""
    MIN_AMOUNT = 50
    MAX_AMOUNT = 500

    def __init__(self):
        self.balance: int = 0
        self.lock = threading.Lock()


    def deposit(self):
        """Совершает 100 транзакций пополнения средств"""
        for _ in range(100):
            amount_deposit = randint(self.MIN_AMOUNT, self.MAX_AMOUNT)
            self.balance += amount_deposit
            print(f"Пополнение: {amount_deposit}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)


    def take(self):
        """Совершает 100 транзакций снятия средств"""
        for _ in range(100):
            amount = randint(self.MIN_AMOUNT, self.MAX_AMOUNT)
            print(f"Запрос на {amount}")
            if amount > self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')