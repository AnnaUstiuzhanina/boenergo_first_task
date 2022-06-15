from time import sleep

from calculator import Calculator

if __name__ == '__main__':

    print('Вычисление квадратичного уравнения вида a*x^2 + b*x + c = 0 с округлением результата до двух знаков после запятой.')
    sleep(1)

    a = 0
    while a == 0:
        a = float(input('Введите значение коэффициента a, не равное 0: '))

    b = float(input('Введите значение коэффициента b: '))
    c = float(input('Введите значение коэффициента c: '))

    calculator = Calculator(a, b, c)
    result = calculator.run()
    print(result)
