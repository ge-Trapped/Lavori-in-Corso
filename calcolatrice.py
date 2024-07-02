def somma(a: int | float, b: int | float) -> int | float:
    return a + b

def divisione(num: int | float, den: int | float) -> float:
    if den == 0:
        raise ValueError
    return num / den

# Aggiungi la funzione sottrazione

# Aggiungi la funzione moltiplicazione

# Aggiungi una funzione magicNumbers per restituire una lista di tutti e soli i numeri dispari
# e multipli di 5 tra start e stop

# Bonus: prevedi di usare l'operatore in nell'assert