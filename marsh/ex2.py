class Marsh:
    def __init__(self, begin, end, number):
        self.begin = begin
        self.end = end
        self.number = number
    def print_info(self):
        print(f"{self.begin} - {self.end}")

    def get_number(self):
        return self.number
    
marshes = []
with open('marsh/marshes.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        begin = lines[i].strip()
        end = lines[i+1].strip()
        number = int(lines[i+2].strip())
        marshes.append(Marsh(begin, end, number))

suggested_marsh = int(input("Введіть номер маршруту: "))
found = False
for marsh in marshes:
    if suggested_marsh == marsh.get_number():
        marsh.print_info()
        found = True

if not found:
    print(f"Маршрут з номером {suggested_marsh} не існує.")



        