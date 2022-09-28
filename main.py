import random
input_number = 0
number_to_guess = random.randint(0, 10)

print("Угадай цифру!")
while input_number != number_to_guess:
    input_number = int(input("Введите число: "))
    if input_number > number_to_guess:
        print("Попробуйте ещё раз! Ваше число больше")
    elif input_number < number_to_guess:
        print("Попробуйте ещё раз! Ваше число меньше")
    else:
        print("Поздравляем, вы угадали!")
print("Игра окончена")