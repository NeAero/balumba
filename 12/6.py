print('Палиндром')
word = input('Введите слово: ')
word_list = list(word)
reserved_word = word_list[::-1]
if word_list == reserved_word:
    print(f'{word} является палиндромом')
else:
    print(f'{word} не является палиндромом')
