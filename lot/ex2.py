class Lot:
    def __init__(self, name, lot_number, lot_type):
        self.name = name
        self.lot_number = lot_number
        self.lot_type = lot_type

    def print_lot(self):
        print("Назва пункту призначення рейсу:", self.name)
        print("Номер рейсу:", self.lot_number)
        print("Тип літака:", self.lot_type)

    def get_name(self):
        return self.name

lots = []
with open('lot/lots.txt', 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        lot_number = lines[i+1].strip()
        lot_type = lines[i+2].strip()
        lots.append(Lot(name, lot_number, lot_type))

suggested_name = input("Введіть обрану назву пункту призначення рейсу: ")
found = False
for lot in lots:
    if lot.get_name() == suggested_name:
        lot.print_lot()
        found = True

if not found:
    print(f"Пункт призначення {suggested_name} не знайдено.")
