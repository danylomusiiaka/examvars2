n = int(input("Enter n: "))
m = int(input("Enter m: "))

matrix = []
print("Enter elements of matrix: ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    max_index = i
    for j in range(m):
        if matrix[i][j] > matrix[i][max_index]:
            max_index = j
    matrix[i][i], matrix[i][max_index] = matrix[i][max_index], matrix[i][i]

print("Матриця після перетворень:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()