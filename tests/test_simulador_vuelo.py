import unittest
from simulador_vuelo import SimuladorVuelo

class TestSimuladorVuelo(unittest.TestCase):

    def test_despegar(self):
        avion = SimuladorVuelo()
        resultado = avion.despegar()
        self.assertEqual(avion.altitud, 10000) 
        self.assertEqual(resultado, "Avión en altitud de crucero")

    def test_aterrizar(self):
        avion = SimuladorVuelo(altitud=10000)
        resultado = avion.aterrizar()
        self.assertEqual(avion.altitud, 0)  
        self.assertEqual(resultado, "El avión ha aterrizado")

    def test_cambiar_direccion(self):
        avion = SimuladorVuelo()
        resultado = avion.cambiar_direccion("oeste")
        self.assertEqual(avion.direccion, "oeste")  
        self.assertEqual(resultado, "Dirección cambiada a oeste")

if __name__ == '__main__':
    unittest.main()

