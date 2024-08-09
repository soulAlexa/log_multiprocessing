class StrNotCorrect(Exception):
    pass
def some_func(chek):
    if not chek:
        raise StrNotCorrect('Empty String')
    if ' ' in chek:
        raise StrNotCorrect('There is a space in the line')

def some_func_2(chek):
    if chek != '1' and chek != '2' and chek != '3' and chek != '4' and chek != '5' and chek != '6' and chek != '7' and chek != '8' and chek != '9' and chek != '0' and chek != '-':
        raise StrNotCorrect('STR not number')

def some_func_3():
    raise StrNotCorrect('StrintToNumber')