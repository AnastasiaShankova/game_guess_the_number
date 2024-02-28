import random


def attempt_pl_1():
    player_1 = ""
    while type(player_1) != int or player_1 not in range(a, b+1):
        try:
            player_1 = input(f"Игрок 1: Назовите число:")
            player_1 = int(player_1)
            if player_1 not in range(a, b+1):
                print("Число выходит за рамки диапазона.")
            elif player_1 in range(a, b+1):
                break
        except ValueError:
            print("Используйте для ввода только цифры из указанного диапазона!")
    return check_value(player_1)


def attempt_pl_2():
    player_2 = ""
    while type(player_2) != int or player_2 not in range(a, b+1):
        try:
            player_2 = input(f"Игрок 2: Назовите число:")
            player_2 = int(player_2)
            if player_2 not in range(a, b+1):
                print("Число выходит за рамки диапазона.")
            elif player_2 in range(a, b+1):
                break
        except ValueError:
            print("Используйте для ввода только цифры указанного диапазона!")
    return check_value(player_2)


def check_value(item):
    if item != value:
        global count
        count -= 1
        print(f"{item}: число указано не верно")
    elif item == value:
        count = 0
        print(f"{item}: Вы выиграли!!!")


def main():
    global a
    a = int(input("Укажите нижнюю границу диапазона:"))
    global b
    b = int(input("Укажите верхнюю границу диапазона:"))
    global value
    value = random.randint(a, b)
    global count
    count = b/2
    print(f"Загадано число в диапазоне от {a} до {b} включительно."
          f"У вас {count} попыток угадать загаданное число.")
    while count > 0:
        attempt_pl_1()
        if count != 0:
            attempt_pl_2()
    else:
        print("Игра окончена!")


main()
