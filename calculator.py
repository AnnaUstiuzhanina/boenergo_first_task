from math import pow, sqrt
from typing import List, Union


class Calculator:

    def __init__(self, a:Union[int, float], b:Union[int, float], c:Union[int, float]) -> None:
        self._a = a
        self._b = b
        self._c = c

    def run(self) -> str:
        result = self._calculate()

        if result == None:
            return 'У уравнения нет корней.'

        elif type(result) == list:
            return f'Корни уравнения: {result[0]}, {result[1]}.'

        else:
            return f'Корень уравнения: {result}.'

    def _discriminant(self) -> Union[int, float]:
        return pow(self._b, 2) - 4 * self._a * self._c

    def _calculate(self) -> Union[int, float]:
        descriminant = self._discriminant()

        if descriminant < 0:
            return None

        elif descriminant == 0:
            return self._one_result()

        elif descriminant > 0:
            return self._two_results()

    def _one_result(self) -> Union[int, float]:

        result = -(self._b / (2 * self._a))

        return self._correct_type(result)

    def _two_results(self) -> List[Union[int, float]]:

        first_result = (-(self._b) + sqrt(pow(self._b, 2) - 4 * self._a * self._c)) / (2 * self._a)
        second_result = (-(self._b) - sqrt(pow(self._b, 2) - 4 * self._a * self._c)) / (2 * self._a)

        return [self._correct_type(first_result), self._correct_type(second_result)]

    def _correct_type(self, result:Union[int, float]) -> Union[int, float]:

        result = round(result, 2)

        if round(result) == result:
            return int(result)
        else:
            return result
