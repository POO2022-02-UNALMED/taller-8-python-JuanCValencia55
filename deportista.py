class Deportista:
    def __init__(self, deporte = "", añosPracticados = 0):
        self._deporte = deporte
        self._añosPracticando = añosPracticados;

    #setters y getters
    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando