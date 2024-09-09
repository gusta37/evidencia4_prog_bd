class SimuladorVuelo:
    def __init__(self, altitud=0, velocidad=0, direccion="norte"):
        self.altitud = altitud
        self.velocidad = velocidad
        self.direccion = direccion

    def despegar(self):
        if self.altitud == 0:
            while self.altitud < 10000:
                self.altitud += 1000
            return "Avión en altitud de crucero"
        return "El avión ya está en el aire"

    def aterrizar(self):
        if self.altitud > 0:
            while self.altitud > 0:
                self.altitud -= 1000
            return "El avión ha aterrizado"
        return "El avión ya está en el suelo"

    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion in ["norte", "sur", "este", "oeste"]:
            self.direccion = nueva_direccion
            return f"Dirección cambiada a {nueva_direccion}"
        return "Dirección no válida"

    def __str__(self):
        return f"Altitud: {self.altitud} ft, Velocidad: {self.velocidad} km/h, Dirección: {self.direccion}"
