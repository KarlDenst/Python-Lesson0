
def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        cell = []
        for j in range(m):
            cell.append(value)
        matrix.append(cell)
    print(matrix)

# ===============================================

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)


