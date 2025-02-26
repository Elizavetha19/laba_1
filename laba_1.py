def digit_to_words(digit):
    digit_dict = {
        '0': "ноль", '1': "один", '2': "два", 
        '3': "три", '4': "четыре", '5': "пять",
    }
    return digit_dict.get(digit, "")


with open("test.txt", "r") as file:
    for line in file.readlines():  # Читаем файл построчно 
        words = line.split()  # Разбиваем строку на числа
            
        for num in words:
            if len(num) > 3 and num[0] in "135" and all(c in "012345" for c in num) and num[-1] in "135":
                    # Находим минимальную и максимальную цифры
                min_digit = min(num)
                max_digit = max(num)
                    # Переводим цифры в пропись
                min_word = digit_to_words(min_digit)
                max_word = digit_to_words(max_digit)

                num_in_words = " ".join(digit_to_words(d) for d in num)

                    # Выводим результат
                print(f"Число прописью: {num_in_words}")
                print(f"Минимальная цифра: {min_digit} ({min_word})")
                print(f"Максимальная цифра: {max_digit} ({max_word})")