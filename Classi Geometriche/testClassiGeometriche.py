import pytest
import classiGeometriche
import math

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

def testTriangolo():
    # Creo un oggetto di tipo Triangolo
    lati = [5, 5, 5]
    angoli = [60, 60, 60]
    t = classiGeometriche.Triangolo(*lati, *angoli)

    # Verifico che p1 sia di tipo Triangolo e di tipo Poligono
    assert isinstance(t, classiGeometriche.Poligono)
    assert isinstance(t, classiGeometriche.Triangolo)

    # Testo il costruttore di Poligono (verificando la correttezza dei dati inizializzati)
    assert t.lati == lati and t.angoli == angoli

    # Verifico il metodo calcolaPerimetro
    assert t.calcolaPerimetro() == sum(lati)

    # Verifico il metodo sommaAngoli
    assert t.sommaAngoli() == sum(angoli)

    assert t.calcolaAltezza() == t.lati[1] * math.sin(t.angoli[1])

    assert t.calcolaAltezza() == pytest.approx(200, rel=1e-5)