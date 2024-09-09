class SimuladorVuelo:
    def __init__(self, altitud=0, velocidad=0, direccion="norte"):
        self.__altitud = altitud
        self.__velocidad = velocidad
        self.__direccion = direccion

    @property
    def altitud(self):
        return self.__altitud

    @altitud.setter
    def altitud(self, valor):
        if valor >= 0:
            self.__altitud = valor
        else:
            raise ValueError("La altitud no puede ser negativa.")

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, valor):
        if valor >= 0:
            self.__velocidad = valor
        else:
            raise ValueError("La velocidad no puede ser negativa.")

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        if nueva_direccion in ["norte", "sur", "este", "oeste"]:
            self.__direccion = nueva_direccion
        else:
            raise ValueError("Dirección no válida. Usa 'norte', 'sur', 'este' o 'oeste'.")

    def despegar(self):
        if self.__altitud == 0:
            while self.__altitud < 10000:
                self.__altitud += 1000
            return "Avión en altitud de crucero"
        return "El avión ya está en el aire"

    def aterrizar(self):
        if self.__altitud > 0:
            while self.__altitud > 0:
                self.__altitud -= 1000
            return "El avión ha aterrizado"
        return "El avión ya está en el suelo"

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        return f"Dirección cambiada a {nueva_direccion}"

    def __str__(self):
        return f"Altitud: {self.__altitud} ft, Velocidad: {self.__velocidad} km/h, Dirección: {self.__direccion}"

