from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre = "", edad = 0, altura = "", sexo ="", añosPracticados = 0,golesMarcados = 0, tarjetasRojas = 0, piernaHabil = ""):
        Persona.__init__(nombre, edad, altura, sexo)
        Deportista.__init__("Futbol", añosPracticados)
        _golesMarcados = golesMarcados
        _tarjetasRojas = tarjetasRojas
        _piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

    #setters y getters
    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas;

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    @classmethod
    def setListaFutbolistas(cls, listaFutbolistas):
        cls._listaFutbolistas = listaFutbolistas;

    #Metodos
    def __str__(self):
        return ("Mi nombre es " + str(self.getNombre()) + " soy profesional en el deporte " + str(self.getDeporte()) + " Tengo " + self.getEdad() + " años de edad y llevo " + self.getAñosPracticando() + " años en el deporte")