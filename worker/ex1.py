n = int(input("Enter n: "))

matrix = []
print("Enter elements of matrix: ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_element = matrix[0][0]
min_index_i = 0
min_index_j = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_index_i = i
            min_index_j = j

row_sum = 0
for j in range(n):
    row_sum += matrix[min_index_i][j]

column_mult = 1
for i in range(n):
    column_mult *= matrix[i][min_index_j]

print("Найменший елемент в матриці:", min_element)
print("Сума елементів в рядку:", row_sum)
print("Добуток елементів в стовпці:", column_mult)