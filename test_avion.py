import unittest
from avion import Avion  # Importaremos la clase Avion después de crearla

class TestAvion(unittest.TestCase):
    
    def test_despegar(self):
        avion = Avion()
        avion.despegar()
        self.assertEqual(avion.en_vuelo, True)
        self.assertEqual(avion.altitud, 1000)  # Altitud inicial después de despegar

    def test_aterrizar(self):
        avion = Avion()
        avion.despegar()
        avion.aterrizar()
        self.assertEqual(avion.en_vuelo, False)
        self.assertEqual(avion.altitud, 0)

    def test_cambiar_altitud(self):
        avion = Avion()
        avion.despegar()
        avion.cambiar_altitud(5000)
        self.assertEqual(avion.altitud, 5000)
    
    def test_altitud_no_cambia_en_tierra(self):
        avion = Avion()
        avion.cambiar_altitud(5000)  # No debería cambiar ya que no está en vuelo
        self.assertEqual(avion.altitud, 0)

if __name__ == '__main__':
    unittest.main()
