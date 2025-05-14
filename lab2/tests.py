import math
from scipy.special import gammaincc
import numpy as np


def pobit_test(sequence: str, sqrt_2: float) -> float:
    """
    Функция подсчитывает частоту встречаемости единиц и на основе этого вычисляет P значение

    :param sequence: Обрабатываемая последовательность

    :return: Возвращает P значение
    """
    N = len(sequence)
    x = [1 if char == "1" else -1 for char in sequence]
    S_N = sum(x)/math.sqrt(N)
    P = math.erfc(S_N/sqrt_2)
    return P

def test_on_repeat_bit(sequence: str) -> float:
    """
    Функция оценивает случайность последовательности на основе знакопеременности, учитывая необходимое кол-во
    единиц в последовательности

    :param sequence: Обрабатываемая последовательность

    :return: Возвращает P значение

    """
    N = len(sequence)
    
    count_ones = sequence.count('1')
    sigma = count_ones/N

    if abs(sigma-0.5) < 2/math.sqrt(N):
        vn = sum(1 for i in range(N-1) if sequence[i] != sequence[i+1])
        P = math.erfc((abs(vn-2*N*sigma*(1-sigma))) / (2*math.sqrt(2*N*sigma*(1-sigma))))
        return P
    else:
        return 0.0


def test_with_blocks(sequence: str, M: int, pi) -> float:
    """
    Функция разбивает последовательность на блоки длиной 8 бит, вычисляет максимальное количество идущих подряд
    единиц в каждом из них и подсчитывает кол-во блоков с определёнными количествами единиц. Затем производится 
    подстановка в формулы и вычисляется значение P

    :param sequence: Обрабатываемая последовательность
    
    :return: Возвращает P значение

    """

    N = len(sequence) 

    blocks = [sequence[i:i+M] for i in range(0, N, M) if i+M <= N]

    V = [0, 0, 0, 0]
    for block in blocks:
        max_ones = 0
        current_ones = 0
        for bit in block:
            if bit == '1':
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
        if max_ones > 0:  
            if max_ones <= len(V):  
                V[max_ones-1] += 1
    V = np.array(V)

    X_squared = np.sum(((V-16*pi)**2)/(16*pi))

    P = gammaincc(3/2, X_squared/2)

    return P
