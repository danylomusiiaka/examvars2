n = int(input("Enter n: "))
m = int(input("Enter m: "))

matrix = []
print("Enter elements of matrix: ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()


special_count = 0
for j in range(len(matrix[0])):  
    column_sum = sum(matrix[i][j] for i in range(len(matrix))) 
    for i in range(len(matrix)):
        if matrix[i][j] > column_sum - matrix[i][j]:
            special_count += 1
            print("Special element:", matrix[i][j])

print("Number of special elements:", special_count)