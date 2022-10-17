"""
Создать калькулятор для работы с рациональными и комплексными числами,
организовать меню, добавив в неё систему логирования.

"""
from op import real_calc
from calc_complex import complex_calc
from fractions import Fraction


def write_to_log(filename='logfile.txt', data: list = []):
    with open(filename, 'a') as output:
        output.write(" = ".join(data))
        output.write('\n')


def get_expression(phrase: str) -> str:
    result = input(phrase)
    result = result.strip()
    result = result.replace(',', '.')
    result = result.replace('\\', '/')
    return result


def is_complex(value: str) -> bool:
    return 'j' in value


def is_real(value: str):
    pass


def parse_text(line: str) -> int:
    line_sp = line.split()
    if len(line_sp) != 3:
        return 0
    elif not line_sp[1] in '-+/*':
        return 0
    elif is_complex(line_sp[0]) or is_complex(line_sp[2]):
        return 1
    else:
        return 2


def convert_operation(value: str) -> int:
    if value == '+':
        return 0
    elif value == '-':
        return 1
    elif value == '*':
        return 2
    elif value == '/':
        return 3
    # elif value == '%': return 4
    # else:


def convert_to_complex(expresion: str) -> dict:
    values = expresion.split()
    result = {'op': convert_operation(values[1]), 'x': complex(values[0]), 'y': complex(values[2])}
    return result


def convert_to_fraction(expresion: str) -> dict:
    values = expresion.split()
    result = {'op': convert_operation(values[1]), 'x': Fraction(values[0]), 'y': Fraction(values[2])}
    return result


def main():
    start = True
    question = 'Введите выражение, которое нужно вычислить. Числа и знаки отделяйте пробелом. Например 2 + 2 или 7-2j + 3+4j для комплексных чисел. И нажмите enter: \n'
    question2 = 'Если хотите продолжить нажмите ENTER. Чтобы выйти введите: выход '

    while start:
        expression = get_expression(question)
        select_calc = parse_text(expression)
        if select_calc == 1:
            d = convert_to_complex(expression)
            try:
                result = complex_calc(d)
            except ZeroDivisionError:
                print('Деление на ноль не допускается!')
        elif select_calc == 2:
            d = convert_to_fraction(expression)
            try:
                result = real_calc(d)
            except ZeroDivisionError:
                result = 'Деление на ноль не допускается!'
        else:
            result = 'Ошибка ввода!'

        write_to_log(data=[expression, str(result)])

        if result != None:
            print(result)
        answer = get_expression(question2)
        if answer.lower() == 'выход':
            start = False


if __name__ == '__main__':
    main()
