import unittest
from horarios import Curso

class TestCurso(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test
        self.curso = Curso("Matemáticas", "MAT101")

    def test_agregar_clase(self):
        self.curso.agregar_clase("Lunes", "10:00")
        self.assertIn("Lunes", self.curso.horario)
        self.assertIn("10:00", self.curso.horario["Lunes"])

    def test_eliminar_clase(self):
        self.curso.agregar_clase("Lunes", "10:00")
        self.curso.eliminar_clase("Lunes", "10:00")
        self.assertNotIn("Lunes", self.curso.horario)

    def test_buscar_clase(self):
        self.curso.agregar_clase("Martes", "12:00")
        resultado = self.curso.buscar_clase("Martes")
        self.assertIn("12:00", resultado)

    def test_filtrar_por_hora(self):
        self.curso.agregar_clase("Miércoles", "09:00")
        dias = self.curso.filtrar_por_hora("09:00")
        self.assertIn("Miércoles", dias)

if __name__ == "__main__":
    unittest.main()
