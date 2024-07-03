import pytest
import classiGeometriche

def testPoligono():
    # Creo un oggetto di tipo Poligono
    lati = [5, 5, 5]
    angoli = [60, 60, 60]
    p = classiGeometriche.Poligono(lati = lati, angoli = angoli)

    # Verifico che p1 è di tipo Poligono
    assert isinstance(p, classiGeometriche.Poligono)

    # Testo il costruttore di Poligono (verificando la correttezza dei dati inizializzati)
    assert p.lati == lati and p.angoli == angoli

    # Verifico il metodo calcolaPerimetro
    assert p.calcolaPerimetro() == sum(lati)

    # Verifico il metodo sommaAngoli
    assert p.sommaAngoli() == sum(angoli)