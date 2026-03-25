import datetime

def ordenar_horas(horas):
    return sorted(horas, key=lambda h: datetime.datetime.strptime(h, "%H:%M").time())

class Curso:
    def __init__(self, nombre, codigo):
        # Inicializa un curso con nombre, código y horario vacío
        self.nombre = nombre
        self.codigo = codigo
        self.horario = {}  # clave: día, valor: lista de horas

    def agregar_clase(self, dia, hora):
        # Agrega una hora de clase a un día específico
        if dia not in self.horario:
            self.horario[dia] = []
        if hora not in self.horario[dia]:
            self.horario[dia].append(hora)

    def eliminar_clase(self, dia, hora):
        # Elimina una hora específica de un día
        if dia in self.horario and hora in self.horario[dia]:
            self.horario[dia].remove(hora)
            if not self.horario[dia]:
                del self.horario[dia]

    def buscar_clase(self, dia):
        # Devuelve la lista de horas de clase para un día
        return self.horario.get(dia, [])

    def mostrar_horario(self):
        # Muestra el horario completo del curso
        for dia in sorted(self.horario):
            horas = ", ".join(ordenar_horas(self.horario[dia]))
            print(f"{dia}: {horas}")

    def filtrar_por_hora(self, hora_busqueda):
        # Devuelve los días donde existe una clase a una hora específica
        return [dia for dia, horas in self.horario.items() if hora_busqueda in horas]


class GestorHorarios:
    def __init__(self):
        # Inicializa una lista de cursos
        self.cursos = []

    def crear_curso(self, nombre, codigo):
        # Crea un nuevo curso si el código es único
        if any(c.codigo == codigo for c in self.cursos):
            print("Error: Ya existe un curso con ese código.")
            return
        curso = Curso(nombre, codigo)
        self.cursos.append(curso)

    def obtener_curso(self, codigo):
        # Busca un curso por su código
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        print("Curso no encontrado.")
        return None

    def mostrar_todos_los_horarios(self):
        # Muestra los horarios de todos los cursos registrados
        for curso in self.cursos:
            print(f"\nCurso: {curso.nombre} ({curso.codigo})")
            curso.mostrar_horario()


def menu():
    gestor = GestorHorarios()
    while True:
        print("\n--- Menú ---")
        print("1. Crear curso")
        print("2. Agregar clase")
        print("3. Eliminar clase")
        print("4. Buscar clases por día")
        print("5. Filtrar días por hora")
        print("6. Mostrar horario de curso")
        print("7. Mostrar todos los horarios")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del curso: ")
            codigo = input("Código único del curso: ")
            gestor.crear_curso(nombre, codigo)

        elif opcion == "2":
            codigo = input("Código del curso: ")
            curso = gestor.obtener_curso(codigo)
            if curso:
                dia = input("Día de la clase: ")
                hora = input("Hora (HH:MM): ")
                curso.agregar_clase(dia, hora)

        elif opcion == "3":
            codigo = input("Código del curso: ")
            curso = gestor.obtener_curso(codigo)
            if curso:
                dia = input("Día: ")
                hora = input("Hora: ")
                curso.eliminar_clase(dia, hora)

        elif opcion == "4":
            codigo = input("Código del curso: ")
            curso = gestor.obtener_curso(codigo)
            if curso:
                dia = input("Día a buscar: ")
                clases = curso.buscar_clase(dia)
                print(f"Clases el {dia}: {', '.join(clases) if clases else 'ninguna'}")

        elif opcion == "5":
            codigo = input("Código del curso: ")
            curso = gestor.obtener_curso(codigo)
            if curso:
                hora = input("Hora (HH:MM): ")
                dias = curso.filtrar_por_hora(hora)
                print(f"Días con clase a las {hora}: {', '.join(dias) if dias else 'ninguno'}")

        elif opcion == "6":
            codigo = input("Código del curso: ")
            curso = gestor.obtener_curso(codigo)
            if curso:
                curso.mostrar_horario()

        elif opcion == "7":
            gestor.mostrar_todos_los_horarios()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
