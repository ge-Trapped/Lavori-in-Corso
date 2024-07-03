import math

# Definire le seguenti classi:
# 1. Poligono: contiene un costruttore e un attributo lati che deve essere una lista di interi, ed una lista di angoli, 
#              che devono essere interi. 
#              Deve contenere inoltre anche un metodo perimetro per calcolarne il perimetro, ed un metodo sommaAngoli
#              per calcolare la somma degli angoli.

# Definisco la classe Poligono
class Poligono:
    # Definisco il costruttore
    def __init__(self, lati: list[int], angoli: list[int]):
        self.lati: list[int] = lati
        self.angoli: list[int] = angoli

    # Definisco il metodo calcolaPerimetro
    def calcolaPerimetro(self) -> int:
        perimetro = 0
        for lato in self.lati:
            perimetro += lato

        # Analogo a
        # return sum(self.lati)

        return perimetro
    
    # Definisco il metodo sommaAngoli
    def sommaAngoli(self) -> int:
        somma = 0
        for angolo in self.angoli:
            somma += angolo

        return somma

# 2. Triangolo: che estende Poligono, con un appropriato costruttore, un metodo calcolaArea ed un metodo calcola altezza
# Definisco la classe Triangolo che eredita da Poligono
class Triangolo(Poligono):
    # Definisco il costruttore
    def __init__(self, lato1: int, lato2: int, lato3: int, angolo1: int, angolo2: int, angolo3: int):
        #self.lati = [lato1, lato2, lato3]
        #self.angoli = [angolo1, angolo2, angolo3]

        # Analogo a
        super().__init__(lati = [lato1, lato2, lato3], angoli = [angolo1, angolo2, angolo3])
        self.base = self.lati[0]
        self.calcolaAltezza()
        # self.lato[0] è la base

    # Definisco un metodo per calcolare l'altezza
    def calcolaAltezza(self):
        self.altezza = self.lati[1] * math.sin(self.angoli[1])

    # Definisco il metodo calcolaArea
    def calcolaArea(self) -> int | float:
        return self.base * self.altezza / 2
    
    def __str__(self) -> str:
        return f"lati: {self.lati} -- angoli: {self.angoli} -- base: {self.base} -- altezza: {self.altezza:.2f}"

    def __eq__(self, other) -> bool:
        return self.lati == other.lati and self.angoli == other.angoli

    def __add__(self, other) -> float:
       return self.calcolaArea() + other.calcolaArea() 

# 3. TriangoloRettangolo: che sovrascrive il metodo per calcolare l'altezza.
class TriangoloRettangolo(Triangolo):
    # Definisco il costruttore
    def __init__(self, lato1: int, lato2: int, lato3: int, angolo1: int, angolo2: int, angolo3: int):
        if 90 in [angolo1, angolo2, angolo3]:
            super().__init__(lato1, lato2, lato3, angolo1, angolo2, angolo3)
            self.base = self.lati[0]
            self.calcolaAltezza()
        else:
            print(f"Errore: nessuno tra gli angoli specificati è retto. angoli: {angolo1, angolo2, angolo3}")
            raise ValueError
        
    def calcolaAltezza(self):
        self.altezza = self.lati[1]

# 4. TriangoloIsoscele: che sovrascrive i metodi calcolaAltezza e calcolaPerimetro
class TriangoloIsoscele(Triangolo):
    def __init__(self, base: int, latoObliquo: int, angoloBase: int, angoloAltezza: int):
        super().__init__(base, latoObliquo, latoObliquo, angoloBase, angoloAltezza, angoloBase)

    # def calcolaAltezza(self):
    #     super().calcolaAltezza()

    def calcolaPerimetro(self):
        return self.lati[0] + 2*self.lati[1]

# 5. TriangoloEquilatero: che sovrascrive i metodi calcolaAltezza e calcolaPerimetro
class TriangoloEquilatero(Triangolo):
    def __init__(self, lato: int):
        super().__init__(lato, lato, lato, 60, 60, 60)

    def calcolaPerimetro(self) -> int:
        return self.lati[0] * 3

def eTriangoloRettangolo(t1: Triangolo):
    # Deve rispettare il teorema di Pitagora
    # uno dei tre lati è l'ipotenusa: è la radice quadrata della somma dei quadrati degli altri due lati
    # ipotenusa = sqrt(cateto1**2 + cateto2 ** 2)
    lati = t1.lati.copy()
    
    for ipotenusa in t1.lati:
        sommaDeiQuadrati = 0
        lati.remove(ipotenusa)
        
        for cateto in lati:
            sommaDeiQuadrati += cateto**2    
        
        if ipotenusa == math.sqrt(sommaDeiQuadrati):
            return True
        
        return False 

# Testa tutte le classi definite, creando opportuni oggetti ed invocando opportunamente tutti i metodi.

# BONUS 1: prevedi che un oggetto di ciascuna classe possa essere stampato con print(), 
#     così come un funzionamento per gli operatori == e +

# BONUS 2: scrivi una funzione per sommare due Poligoni e testala con due poligoni qualsiasi 
#          e poi con due rettangoli qualsiasi. 

def sommaPoligoni(p1: Poligono, p2: Poligono):
    return p1.calcolaPerimetro() + p2.calcolaPerimetro()

# Test


p1 = Poligono(lati = [3, 4, 5], angoli = [90, 45, 45])
print(p1.calcolaPerimetro())



lati = [3, 4, 5]
angoli = [90, 45, 45]

t1 = Triangolo(*lati, *angoli) # sequence unpacking
t2 = Triangolo(3, 4, 5, 90, 60, 30) # sequence unpacking
print(t1.calcolaPerimetro())

assert isinstance(t1, Poligono)

# angoli = [30, 30, 90]
# tr1 = TriangoloRettangolo(*lati, *angoli)
# print(tr1.altezza)

# teq1 = TriangoloEquilatero(4)
# teq2 = TriangoloEquilatero(5)
# print(teq1)
# print(teq1 == teq2)
# print(t1 + t2)

# print(sommaPoligoni(p1, t1))

