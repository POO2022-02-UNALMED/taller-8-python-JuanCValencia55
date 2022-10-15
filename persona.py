class Persona:
    
    #Constructor
    def __init__(self, nombre = "", edad = 0, altura = "", sexo =""):
        _nombre = nombre
        _edad = edad
        _altura = altura
        _sexo = sexo

    #getters y setters
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setEdad(self, edad):
        self._edad = edad

    def setAltura(self, altura):
        self._altura = altura

    def setSexo(self, sexo):
        self._sexo = sexo
