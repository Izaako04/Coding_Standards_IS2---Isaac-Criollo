"""Módulo de definición de la clase Student y demostración de su uso."""

class Student:
    """Clase que representa a un estudiante y su rendimiento académico."""

    def __init__(self, student_id, name):
        """Inicializa un nuevo estudiante con ID, nombre y atributos vacíos."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.passed = False
        self.honor = "Unknown"
        self.letter = "N/A"

    def add_grades(self, grade):
        """Agrega una calificación si es numérica."""
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Ignorado: {grade} no es un número")

    def calc_average(self):
        """Calcula el promedio de calificaciones."""
        if not self.grades:
            print("No hay calificaciones.")
            return 0.0
        avg = sum(self.grades) / len(self.grades)
        self.set_letter(avg)
        return avg

    def set_letter(self, avg):
        """Asigna una calificación literal según el promedio."""
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
            self.honor = "Deficient"

    def remove_grade_by_position(self, index):
        """Elimina una calificación por su índice."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Índice fuera de rango: {index}")

    def report(self):
        """Imprime el reporte académico del estudiante."""
        avg = self.calc_average()
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Avg Grade: {avg:.2f}")
        print(f"Final Grade = {self.letter}")
        print(f"Honor: {self.honor}")

def start_run():
    """Función principal para probar la clase Student."""
    student = Student("x", "Carlos")
    student.add_grades(100)
    student.add_grades(50)
    student.calc_average()
    student.remove_grade_by_position(1)
    student.check_honor()
    student.report()

if __name__ == "__main__":
    start_run()
