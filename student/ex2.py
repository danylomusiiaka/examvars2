class Student:
    def __init__(self, name, group_number, performance):
        self.name = name
        self.group_number = group_number
        self.performance = performance

    def print_student(self):
        print("Прізвище та ім'я:", self.name)
        print("Номер групи:", self.group_number)
        print("Успішність:", self.performance)

    def average_score(self):
        return sum(self.performance) / len(self.performance)


students = []
with open('student/students.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        group_number = lines[i+1].strip()
        performance = list(map(int, lines[i+2].strip().split()))[:5]
        students.append(Student(name, group_number, performance))

for student in students:
    if student.average_score() > 4.0:
        student.print_student()
        print("Середнє арифметичне:", student.average_score())