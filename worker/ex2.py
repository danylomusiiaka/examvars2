class Worker:
    def __init__(self, name, position, year):
        self.name = name
        self.position = position
        self.year = year

    def print_worker(self):
        print("Прізвище та ініціали працівника:", self.name)
        print("Назва посади:", self.position)
        print("Рік поступлення на роботу:", self.year)

    def get_year(self):
        return self.year


workers = []
with open('worker/workers.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        position = lines[i+1].strip()
        year = int(lines[i+2].strip())
        workers.append(Worker(name, position, year))

suggested_year = int(input("Введіть стаж роботи: "))
found = False
for worker in workers:
    if worker.get_year() == suggested_year:
        worker.print_worker()
        found = True

if not found:
    print(f"Не знайдемо працівників зі стажем {suggested_year}")