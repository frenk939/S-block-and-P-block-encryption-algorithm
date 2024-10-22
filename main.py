# S-блок (довільна таблиця замін)
S_BOX = {
    0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
    0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
    0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
    0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
}


# Функція для S-блоку
def s_block(input_byte):
    high_nibble = (input_byte >> 4) & 0xF
    low_nibble = input_byte & 0xF
    new_high_nibble = S_BOX[high_nibble]
    new_low_nibble = S_BOX[low_nibble]
    return (new_high_nibble << 4) | new_low_nibble


# Зворотний S-блок
INV_S_BOX = {v: k for k, v in S_BOX.items()}


def inv_s_block(input_byte):
    high_nibble = (input_byte >> 4) & 0xF
    low_nibble = input_byte & 0xF
    new_high_nibble = INV_S_BOX[high_nibble]
    new_low_nibble = INV_S_BOX[low_nibble]
    return (new_high_nibble << 4) | new_low_nibble


# P-блок (перестановка бітів)
P_BOX = [7, 6, 5, 4, 3, 2, 1, 0]


def p_block(input_byte):
    output_byte = 0
    for i in range(8):
        bit = (input_byte >> i) & 0x1
        output_byte |= (bit << P_BOX[i])
    return output_byte


# Зворотний P-блок
INV_P_BOX = [P_BOX.index(i) for i in range(8)]


def inv_p_block(input_byte):
    output_byte = 0
    for i in range(8):
        bit = (input_byte >> i) & 0x1
        output_byte |= (bit << INV_P_BOX[i])
    return output_byte


# Шифрування
def encrypt(input_byte):
    s_block_output = s_block(input_byte)
    encrypted_byte = p_block(s_block_output)
    return encrypted_byte


# Дешифрування
def decrypt(input_byte):
    p_block_output = inv_p_block(input_byte)
    decrypted_byte = inv_s_block(p_block_output)
    return decrypted_byte


# Функція для перевірки коректності введеного двійкового числа
def validate_binary_input(binary_str):
    try:
        if binary_str.startswith('0b') and len(binary_str) <= 10:  # '0b' + 8 біт = максимум 10 символів
            input_data = int(binary_str, 2)  # Перетворення з двійкового у ціле число
            if 0 <= input_data <= 255:
                return input_data
        print("Помилка: введіть коректне двійкове число (8 біт).")
        return None
    except ValueError:
        print("Помилка: введіть коректне двійкове число.")
        return None


# Функція для виведення результатів з фіксованим 8-бітним форматом
def format_binary_output(output_byte):
    return f"0b{output_byte:08b}"


# Функція для відображення меню
def menu():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Шифрувати дані")
        print("2. Дешифрувати дані")
        print("3. Вийти")
        choice = input("Виберіть опцію (1-3): ")

        if choice == "1":
            # Шифрування
            input_binary = input("Введіть 8-бітне двійкове число для шифрування (наприклад, 0b10101010): ")
            input_data = validate_binary_input(input_binary)
            if input_data is not None:
                encrypted_data = encrypt(input_data)
                print(f"Зашифровані дані: {format_binary_output(encrypted_data)}")

        elif choice == "2":
            # Дешифрування
            input_binary = input("Введіть 8-бітне двійкове число для дешифрування (наприклад, 0b10101010): ")
            input_data = validate_binary_input(input_binary)
            if input_data is not None:
                decrypted_data = decrypt(input_data)
                print(f"Дешифровані дані: {format_binary_output(decrypted_data)}")

        elif choice == "3":
            # Вихід
            print("Вихід з програми.")
            break

        else:
            print("Неправильний вибір. Спробуйте знову.")


# Запуск програми
menu()

"""
Кілька прикладів інших 8-бітних вхідних даних у двійковому вигляді для тестуванн:
0b11010101 (десятковий еквівалент: 213)
0b00101111 (десятковий еквівалент: 47)
0b11110000 (десятковий еквівалент: 240)
0b00001111 (десятковий еквівалент: 15)
0b10101010 (десятковий еквівалент: 170)
0b01100110 (десятковий еквівалент: 102)
0b10011001 (десятковий еквівалент: 153)
0b01010101 (десятковий еквівалент: 85)
0b11111111 (десятковий еквівалент: 255)
0b00000000 (десятковий еквівалент: 0)
"""