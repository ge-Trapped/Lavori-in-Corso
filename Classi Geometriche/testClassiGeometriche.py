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
    t2 = classiGeometriche.Triangolo(*lati, *angoli)

    # Verifico che p1 sia di tipo Triangolo e di tipo Poligono
    assert isinstance(t, classiGeometriche.Poligono)
    assert isinstance(t, classiGeometriche.Triangolo)

    # Testo il costruttore di Poligono (verificando la correttezza dei dati inizializzati)
    assert t.lati == lati and t.angoli == angoli

    # Verifico il metodo calcolaPerimetro
    assert t.calcolaPerimetro() == sum(lati)

    # Verifico il metodo sommaAngoli
    assert t.sommaAngoli() == sum(angoli)

    # Verifico il metodo calcolaAltezza
    assert t.calcolaAltezza() == t.lati[1] * math.sin(t.angoli[1])

    # assert t.calcolaAltezza() == pytest.approx(200, rel=1e-5)

    # Verifico il metodo calcolaArea
    assert t.calcolaArea() == t.lati[0] * t.altezza / 2

    # Verifico i metodi dunder
    assert t.__str__() == f"lati: {t.lati} -- angoli: {t.angoli} -- base: {t.base} -- altezza: {t.altezza:.2f}"
    assert t == t2 and (t.lati == t2.lati and t.angoli == t2.angoli)
    assert t + t2 == t.calcolaArea() + t2.calcolaArea()