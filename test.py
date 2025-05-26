class Student:

 def __init__(self,id,name):
    self.id = id
    self.name = name
    self.grades = []
    self.isPassed = "NO"
    self.honor = bool # Should be bool

 def addGrades(self, g):
    if isinstance(g, (int, float)):
            self.grades.append(g)
    else:
        print(f"Ignorado: {g} no es un número")

 def calcAverage(self):
    if len(self.grades) == 0:
            print("No hay calificaciones.")
            return 0
    t = sum(self.grades)
    avg = t / len(self.grades)
    self.setLetter(avg)
    return avg
 
 def setLetter(self, avg):
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

 def checkHonor(self):
    avg = self.calcAverage()
    if avg > 90:
        self.honor = "Extraordinary"
    elif avg < 90 and avg > 60:
            self.honor = "Regular"
    else: 
        self.honor = "Under"

 def removeGradeByPosition(self, index):
    if 0 <= index < len(self.grades):
            del self.grades[index]
    else:
        print(f"Índice fuera de rango: {index}")

 def report(self):
    avg = self.calcAverage()
    print(f"ID: {self.id}")
    print(f"Name: {self.name}")
    print(f"Avg Grade: {avg:.2f}")
    print(f"Final Grade = {self.letter}")
    print(f"Honor: {self.honor}")

def startrun():
    a = Student("x", "Carlos")
    a.addGrades(100)
    a.addGrades(50)
    a.calcAverage()
    a.removeGradeByPosition(1)
    a.checkHonor()
    a.report()

startrun()