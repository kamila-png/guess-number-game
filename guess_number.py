import random

def guess_number_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У тебя 10 попыток, чтобы угадать.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        try:
            user_input = input(f"Попытка {attempt}: Введите число от 1 до 100: ")
            guess = int(user_input)

            if guess < 1 or guess > 100:
                print("Ошибка: число должно быть в диапазоне от 1 до 100.")
                continue

            if guess < number_to_guess:
                print("Слишком маленькое число.")
            elif guess > number_to_guess:
                print("Слишком большое число.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} с {attempt} попытки.")
                break

        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, введите целое число.")

    else:
        print(f"Вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

    # Предложение сыграть ещё раз
    play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
    if play_again == "да":
        guess_number_game()
    else:
        print("Спасибо за игру!")

# Запуск игры
guess_number_game()
