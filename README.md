# Sistema de Gestión de Horarios de Clases

Aplicación desarrollada en Python para gestionar los horarios de distintos cursos, permitiendo organizar, consultar y filtrar clases de forma eficiente.

---

## Tecnologías utilizadas
- Python  
- Programación Orientada a Objetos (POO)  

---

## Funcionalidades
- Creación de cursos con identificador único  
- Gestión de clases (añadir, eliminar y buscar)  
- Consulta del horario completo por curso  
- Filtrado de clases por día y hora  
- Almacenamiento de datos mediante diccionarios  

---

## Conceptos aplicados
- Diseño de clases (`Curso`, `GestorHorarios`)  
- Uso de estructuras de datos (diccionarios y listas)  
- Encapsulación  
- Separación de responsabilidades  

---

## Tests
El proyecto incluye pruebas automatizadas para verificar:
- Añadir clases  
- Eliminar clases  
- Búsqueda por día y hora  
- Filtrado de horarios  

Archivo: `test_horarios.py`

---

## Ejecución
1. Clonar el repositorio  
2. Ejecutar el archivo principal:
```bash
python horarios.py

## Ejemplo de uso

Curso: DAW  
Horario:  
- Lunes: 10:00, 12:00  
- Miércoles: 09:00  

Búsqueda: clases el lunes a las 10:00 → resultado encontrado  
