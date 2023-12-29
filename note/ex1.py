n = int(input("Введіть n: "))

matrix = []
print("Введіть елементи матриці: ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_element = matrix[0][0]
min_index_i = 0
min_index_j = 0

for i in range(n):
    for j in range(n):
        if min_element > matrix[i][j]:
            min_element = matrix[i][j]
            min_index_i = i
            min_index_j = j

print("Найменший елемент матриці:", min_element)

row_sum = 0
for j in range(n):
    row_sum += matrix[min_index_i][j]

print("Сума елементів рядка:", row_sum)

colon_mult = 1
for i in range(n):
    colon_mult *= matrix[i][min_index_j]

print("Добуток елементів стовпця:", colon_mult)