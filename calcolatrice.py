def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def sottrazione(a: int | float, b: int | float) -> int | float:
    return a - b

def moltiplicazione(a: int | float, b: int | float) -> int | float:
    return a * b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

def magicNumbers(start: int, stop:int) -> list:
    return [num for num in range(start, stop)
            if num % 2 != 0 and num % 5 == 0]