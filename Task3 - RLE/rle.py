source_text_file = open('source_text.txt', 'w')
source_text = input('Введите исходный текст: ')
source_text_file.write(source_text)
source_text_file.close()

operation = int(input('Для сжатия напишите 1, для восстановления - 2: '))

if operation == 1:

    source_text_file = open('source_text.txt', 'r')
    source_text = source_text_file.readline()
    source_text_file.close()

    result_file = open('result.txt', 'w')

    compressed_text = ''

    current_char, count = '', 0

    for char in range(len(source_text)):

        if source_text[char] != current_char and count == 0:
            current_char = source_text[char]
            count = 1

        elif source_text[char] != current_char and count > 0:
            compressed_text += str(count) + current_char
            current_char = source_text[char]
            count = 1

        elif source_text[char] == current_char:
            count += 1

        if char == len(source_text)-1:
            compressed_text += str(count) + current_char

    result_file.write(compressed_text)
    result_file.close()

    result_file = open('result.txt', 'r')
    print(f'Отформатированный текст:\n\n"{compressed_text}"\n\nсохранён в файле result.py.')
    result_file.close()

if operation == 2:

    source_text_file = open('source_text.txt', 'r')
    original_source_text = source_text_file.readline()
    source_text = original_source_text
    source_text_file.close()

    result_file = open('result.txt', 'w')

    recovered_text, multipliers_and_letters, multipliers, letters = '', {}, [], []

    for i in range(len(source_text)):
        if source_text[i].isalpha() == True:
            source_text = source_text.replace(source_text[i], '-')
    only_digits = source_text.split('-')
    source_text = original_source_text

    for i in range(len(source_text)):
        if source_text[i].isdigit() == True:
            source_text = source_text.replace(source_text[i], '-')
    only_letters = source_text.split('-')
    source_text = original_source_text

    for i in range(len(only_digits)-1, -1, -1):
        if only_digits[i] == '':
            del only_digits[i]

    for i in range(len(only_letters)-1, -1, -1):
        if only_letters[i] == '':
            del only_letters[i]

    for i in range(len(only_digits)):
        multipliers_and_letters[only_digits[i]] = only_letters[i]

    for key, value in multipliers_and_letters.items():
        recovered_text += int(key)*value
    
    result_file.write(recovered_text)
    result_file.close()

    result_file = open('result.txt', 'r')
    print(f'Отформатированный текст:\n\n"{recovered_text}"\n\nсохранён в файле result.py.')
    result_file.close()
