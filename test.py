"""Student Grade Management System with extended features and pylint compliance."""

from typing import Union


class Student:
    """Class representing a student and their academic performance."""

    def __init__(self, student_id: str, name: str):
        """Initialize a student, validating non-empty ID and name."""
        if not student_id or not name:
            raise ValueError("ID and name cannot be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.passed = False
        self.honor = "Unknown"
        self.letter = "N/A"
        self.honor_roll = False  # Boolean flag for honor roll status

    def add_grades(self, grade: Union[int, float]):
        """Add a grade if it is numeric and between 0 and 100."""
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Invalid input: {grade}. Must be a number between 0 and 100.")

    def calc_average(self) -> float:
        """Calculate average grade and update pass/fail and letter grade."""
        if not self.grades:
            print("No grades available.")
            return 0.0
        avg = sum(self.grades) / len(self.grades)
        self.set_letter(avg)
        self.passed = avg >= 60
        self.honor_roll = avg >= 90
        return avg

    def set_letter(self, avg: float):
        """Assign a letter grade based on the average."""
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
        """Update honor description based on average grade."""
        avg = self.calc_average()
        if avg > 90:
            self.honor = "Extraordinary"
        elif 60 < avg <= 90:
            self.honor = "Regular"
        else:
            self.honor = "Under"

    def remove_grade_by_index(self, index: int):
        """Remove a grade by its index, handling out-of-range errors."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Index out of range: {index}")

    def remove_grade_by_value(self, value: Union[int, float]):
        """Remove the first occurrence of a grade by its value."""
        try:
            self.grades.remove(value)
        except ValueError:
            print(f"Grade value {value} not found in the list.")

    def generate_summary_report(self) -> str:
        """Generate a formatted summary report of the student."""
        avg = self.calc_average()
        pass_status = "Passed" if self.passed else "Failed"
        honor_roll_status = "Yes" if self.honor_roll else "No"
        report = (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {len(self.grades)}\n"
            f"Average Grade: {avg:.2f}\n"
            f"Letter Grade: {self.letter}\n"
            f"Pass/Fail Status: {pass_status}\n"
            f"Honor Roll Status: {honor_roll_status}\n"
        )
        return report

    def report(self):
        """Print the summary report."""
        print(self.generate_summary_report())


def start_run():
    """Main function to test the Student class."""
    try:
        student = Student("001", "Carlos")
        student.add_grades(95)
        student.add_grades(87.5)
        student.add_grades(45)
        student.add_grades("text")  # invalid
        student.add_grades(-10)     # invalid

        student.calc_average()
        student.check_honor()

        # Test removing grades
        student.remove_grade_by_index(10)  # out of range
        student.remove_grade_by_value(100)  # not in list
        student.remove_grade_by_value(87.5)  # valid removal

        student.report()
    except ValueError as error:
        print(f"Error creating student: {error}")


if __name__ == "__main__":
    start_run()
