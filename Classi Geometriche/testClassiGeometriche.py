import pytest
import classiGeometriche

def testPoligono():
    poligono = classiGeometriche.Poligono(lati = [2, 3, 4], angoli = [90, 45, 45])

    assert poligono.calcolaPerimetro() == 9
    assert poligono.sommaAngoli() == 180
    assert isinstance(poligono, classiGeometriche.Poligono)

def testPoligono(lati = [2, 3, 4], angoli = [90, 45, 45]):

    assert classiGeometriche.Poligono.calcolaPerimetro() == 9
    assert classiGeometriche.Poligono.sommaAngoli() == 180
    assert isinstance(classiGeometriche.Poligono)





    # 1. Creo un oggetto di tipo Poligono
    # 2. Testo le sue funzonalità (i suoi metodi, i suoi attributi, i suoi metodi dunder ed il suo tipo)
    # NB: ricorda che puoi verificare con un assert il tipo di un oggetto con la funzione isinstance