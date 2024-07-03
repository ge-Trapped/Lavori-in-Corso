import pytest
import calcolatrice

def testSomma():
    assert calcolatrice.somma(2, 2) == 4, "La funzione somma(2, 2) non ha prodotto 4!"
    assert calcolatrice.somma(3, 3) != 7
    assert calcolatrice.somma(0, -1) < 0

def testSottrazione():
    assert calcolatrice.sottrazione(10, 5) == 5
    assert calcolatrice.sottrazione(0, 0) == 0
    assert calcolatrice.sottrazione(4, 5) < 0

def moltiplicazione():
    assert calcolatrice.moltiplicazione(3, 3) == 9
    assert calcolatrice.moltiplicazione(0, 10) == 0
    assert calcolatrice.moltiplicazione(-2, 2) == -4

def testDivisione():
    assert calcolatrice.divisione(6, 3) == 2
    assert calcolatrice.divisione(10, 5) == 2
    with pytest.raises(ValueError):
        calcolatrice.divisione(1, 0)
        
def testMagicNumbers():
    risultato = calcolatrice.magicNumbers(0, 30)
    assert 5 in risultato
    assert 15 in risultato
    assert 25 in risultato
    assert 30 in risultato