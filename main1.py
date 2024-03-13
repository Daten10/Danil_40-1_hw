from decouple import config
from random import randint


def start_game():
    exit = 1
    print('MY balance: ', config('MY_MONEY'), '$')
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    money = config('MY_MONEY', cast=int)
    while(exit!=0):
        guess = int(input('Выберите число от 1 до 10: '))
        if guess > 10 or guess < 1:
            print('Попробуйте еще раз!')
            continue
        bet = int(input('Сделайте ставку: '))
        if bet > money or bet < 1:
            print('Попробуйте еще раз!')
            continue
        win = list_of_numbers[randint(0,9)]

        if guess == win:
            money = money + bet * 2
            print('Вы выиграли, загаданное число: ', win)
            print('Мой баланс: ', money,'$')

        else:
            money -= bet
            print('Вы проиграли, загаданное число: ', win)
            print('Мой баланс: ', money,'$')

        exit = int(input('введите 0 чтобы выйти: '))
