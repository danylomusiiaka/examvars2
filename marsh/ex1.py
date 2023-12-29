n = int(input("Введіть n: "))

matrix = []
print("Введіть елементи матриці: ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

max_element = matrix[0][0]
max_index_i = 0
max_index_j = 0
for i in range(n):
    for j in range(n):
        if abs(matrix[i][j]) > abs(max_element):
            max_element = matrix[i][j]
            max_index_i = i
            max_index_j = j

new_matrix = []
for i in range(n):
    if i == max_index_i:
        continue
    new_row = []
    for j in range(n):
        if j == max_index_j:
            continue
        new_row.append(matrix[i][j])
    new_matrix.append(new_row)

print("Матриця після перетворень:")
for row in new_matrix:
    for element in row:
        print(element, end=' ')
    print()