import pytest
import calcolatrice

def testSomma():
    assert calcolatrice.somma(2, 2) == 4, "La funzione somma(2, 2) non ha prodotto 4!"
    assert calcolatrice.somma(3, 3) != 7
    assert calcolatrice.somma(0, -1) < 0

def testDivisione():
    assert calcolatrice.divisione(6, 3) == 2
    assert calcolatrice.divisione(10, 5) == 2
    with pytest.raises(ValueError):
        calcolatrice.divisione(1, 0)