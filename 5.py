# 5. Строка считается заглавной, если каждое слово в строке либо (а) пишется с заглавной буквы
# (то есть только первая буква слова в верхнем регистре), либо (б) считается исключением и полностью помещается в строчными буквами,
# если только это не первое слово, которое всегда пишется с большой буквы.
#
# Напишите функцию, которая преобразует строку в заглавный регистр, учитывая необязательный список исключений
# (второстепенные слова). Список второстепенных слов будет представлен в виде строки, где каждое слово отделено пробелом.
# Ваша функция должна игнорировать
# регистр строки второстепенных слов — она должна вести себя так же, даже если регистр строки второстепенных слов изменен.

#примеры:
#title_case('a clash of KINGS', 'a an the of') #
#должен вернуть: 'A Clash of Kings'

# title_case('THE WIND IN THE WILLOWS', 'The In') #
# должен вернуть: 'The Wind in the Willows'
#
# title_case('the quick brown fox') #
# должен вернуть: 'The Quick Brown Fox'

def title_case(a,b=''):
    arr_str = a.split(' ')
    c = arr_str[0]
    arr_ = []
    arr_.append(c.title())
    for i in arr_str[1::]:
        if i.lower() in b.lower():
            arr_.append(i.lower())
        else:
            arr_.append(i.title())
    print(' '.join(arr_))
    return ' '.join(arr_)


def test():
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') ==  'The Quick Brown Fox'
    print('Все прошло успешно!!!')

test()