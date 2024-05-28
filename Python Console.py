def reverse_number(number):
    digit_1 = number // 10000
    digit_2 = (number // 1000) % 10
    digit_3 = (number // 100) % 10
    digit_4 = (number // 10) % 10
    digit_5 = number % 10

    reversed_number = digit_5 * 10000 + digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1

    return reversed_number

user_input = int(input("Введите 5-ти значное число: "))

reversed_result = reverse_number(user_input)

print(f"Результат: {reversed_result}")
