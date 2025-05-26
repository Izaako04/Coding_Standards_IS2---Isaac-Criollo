"""Student Grade Management System - Cumple con todos los requerimientos funcionales."""

class Student:
    """Clase que representa a un estudiante y su rendimiento académico."""

    def __init__(self, student_id, name):
        """Inicializa un nuevo estudiante, validando datos básicos."""
        if not student_id or not name:
            raise ValueError("ID y nombre no pueden estar vacíos.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.passed = False
        self.honor = "Unknown"
        self.letter = "N/A"

    def add_grades(self, grade):
        """Agrega una calificación si es válida (0–100 numérico)."""
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Entrada inválida: {grade}. Debe ser número entre 0 y 100.")

    def calc_average(self):
        """Calcula el promedio de calificaciones y actualiza atributos."""
        if not self.grades:
            print("No hay calificaciones.")
            return 0.0
        avg = sum(self.grades) / len(self.grades)
        self.set_letter(avg)
        self.passed = avg >= 60
        return avg

    def set_letter(self, avg):
        """Asigna una calificación literal basada en el promedio."""
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

    def check_honor(self):
        """Evalúa si el estudiante califica para mención de honor."""
        avg = self.calc_average()
        if avg > 90:
            self.honor = "Extraordinary"
        elif 60 < avg <= 90:
            self.honor = "Regular"
        else:
            self.honor = "Under"

    def remove_grade_by_position(self, index):
        """Elimina una calificación por su índice si es válido."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Índice fuera de rango: {index}")

    def report(self):
        """Imprime el reporte académico del estudiante."""
        avg = self.calc_average()
        pass_status = "Passed" if self.passed else "Failed"
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Avg Grade: {avg:.2f}")
        print(f"Final Grade: {self.letter}")
        print(f"Honor: {self.honor}")
        print(f"Status: {pass_status}")

def start_run():
    """Función principal para probar la clase Student."""
    try:
        student = Student("001", "Carlos")
        student.add_grades(95)
        student.add_grades(87.5)
        student.add_grades(45)
        student.add_grades("texto")  # prueba entrada inválida
        student.add_grades(-10)      # prueba fuera de rango
        student.calc_average()
        student.remove_grade_by_position(10)  # índice inválido
        student.check_honor()
        student.report()
    except ValueError as error:
        print(f"Error al crear estudiante: {error}")

if __name__ == "__main__":
    start_run()
