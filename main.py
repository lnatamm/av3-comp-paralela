from src.client.solver import Solver
import time

# Função somente para a leitura da matriz
def readFile(FILE_PATH):
    file = open(FILE_PATH)
    n, m = map(int, file.readline().split())
    M = []
    for i in range(n):
        M.append([])
        line = file.readline().split()
        for j in range(m):
            M[i].append(float(line[j]))
    return M

M_1 = readFile("matrices/matrix_50x50_a.txt")
M_2 = readFile("matrices/matrix_50x50_b.txt")

# Solver que vai resolver a multiplicação de matrizes
tempo_paraleo = time.time()
solver = Solver()
result = solver.multiply_matrices(M_1, M_2)
print("Resultado da multiplicação:")
for row in result:
    print(row)
print(f"Tempo de execução paralelo: {time.time() - tempo_paraleo:.2f} segundos")

tempo_serial = time.time()
result_serial = []
for i in range(len(M_1)):
    result_serial.append([])
    for j in range(len(M_2[0])):
        result_serial[i].append(0)
        for k in range(len(M_2)):
            result_serial[i][j] += M_1[i][k] * M_2[k][j]

print(f"Tempo de execução serial: {time.time() - tempo_serial:.2f} segundos")