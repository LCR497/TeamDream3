# 6. Напишите функцию to_weird_case,
# которая принимает строку и возвращает ту же строку, в которой все символы с четным индексом в каждом слове
# отображаются в верхнем регистре, а все символы с нечетным индексом в каждом слове — в нижнем регистре.
# Только что объясненная индексация основана на нуле, поэтому нулевой индекс четный, поэтому этот символ должен быть в верхнем регистре,
# и вам нужно начинать заново для каждого слова.
#
# Передаваемая строка будет состоять только из букв алфавита и пробелов (' ').
# Пробелы будут присутствовать только в том случае, если слов несколько. Слова будут разделены одним пробелом (' ').
#
# ПрИмЕрЫ:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
# to_weird_case('This') # => returns 'ThIs'
# to_weird_case('is') # => returns 'Is'
# to_weird_case('This is a test') # => returns 'ThIs Is A TeSt'

def to_weird_case(string):
    result_str = ''
    k = 0
    len_ = len(string)
    print(len_)
    while k < len(string):
        if k % 2 == 0:
            result_str += string[k].upper()
        else:
            result_str += string[k].lower()
        k+=1
    print(result_str)

to_weird_case('This is a test')
