class Note:
    def __init__(self,name,number,date):
        self.name = name
        self.number = number
        self.date = date

    def print_info(self):
        print("Прізвище та ім'я:", self.name)
        print("Номер телефону:", self.number)
        print("День народження (день/місяць/рік):", self.date)

    def get_number(self):
        return self.number


notes = []
with open('note/notes.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        number = lines[i+1].strip()
        date = lines[i+2].strip()
        notes.append(Note(name, number, date))

suggested_number = input("Введіть номер телефону: ")
found = False
for note in notes:
    if suggested_number == note.get_number():
        note.print_info()
        found = True

if not found:
    print(f"Людини з номером {suggested_number} не знайдено.")

