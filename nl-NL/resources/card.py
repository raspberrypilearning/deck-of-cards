class Kaart:

    def __init__(self, kleur, nummer):
        self._kleur = kleur
        self._nummer = nummer

    def __repr__(self):
        return self._nummer + " van " + self._kleur

    @property
    def kleur(self):
        return self._kleur

    @kleur.setter
    def kleur(self, kleur):
           if kleur in ["harten", "klaveren", "ruiten", "schoppen"]:
               self._kleur = kleur
           else:
               print("Dat is geen kleur!")

    @property
    def nummer(self):
        return self._nummer

    @nummer.setter
    def nummer(self, nummer):
        geldig = [str(n) for n in range(2,11)] + ["B", "V", "H", "A"]
        if nummer in geldig:
            self._nummer = nummer
        else:
            print("Dat is geen geldig nummer")


class Spel:

    def __init__(self):
        self._kaarten = []
        self.bevolk()
        #print(self._kaarten)


    def bevolk(self):
        kleuren = ["harten", "klaveren", "ruiten", "schoppen"]
        nummers = [str(n) for n in range(2,11)] + ["B", "V", "H", "A"]
        self._kaarten = [ Kaart(s, n) for s in kleuren for n in nummers ]

    def bevolk2(self):
        kleuren = ["harten", "klaveren", "ruiten", "schoppen"]
        nummers = [str(n) for n in range(2,11)] + ["B", "V", "H", "A"]
        kaarten = []
        for kleur in kleuren:
            for nummer in nummers:
                kaarten.append(Kaart(kleur, nummer))
        self._kaarten = kaarten


spel = Spel()
