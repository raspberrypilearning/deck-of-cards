class Carta:

    def __init__(self, palo, numero):
        self._palo = palo
        self._numero = numero

    def __repr__(self):
        return self._numero + " de " + self._palo

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
           if palo in ["corazones", "trebol", "diamantes", "espadas"]:
               self._palo = palo
           else:
               print("¡Esto no es un palo!")

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        valido = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if numero in valido:
            self._numero = numero
        else:
            print("¡Esto no es un número válido!")


class Baraja:

    def __init__(self):
        self._cartas = []
        self.completar()
        #print(self._cartas)


    def completar(self):
        palos = ["corazones", "trebol", "diamantes", "espadas"]
        numeros = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cartas = [ Carta(p, n) for p in palos for n in numeros ]

    def completar2(self):
        palos = ["corazones", "trebol", "diamantes", "espadas"]
        numeros = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        cartas = []
        for palo in palos:
            for numero in numeros:
                cartas.append(Carta(palo, numero))
        self._cartas = cartas


baraja = Baraja()
