from src.client.solver import Solver
def readFile(FILE_PATH):
    file = open(FILE_PATH)
    n, m = file.readline().split()
    n = int(n)
    m = int(m)
    M = []
    for i in range(n):
        M.append([])
        line = file.readline().split()
        for j in range(m):
            M[i].append(float(line[j]))
    return M

M_1 = readFile("matrix1.txt")
M_2 = readFile("matrix2.txt")

solver = Solver()
result = solver.multiply_matrices(M_1, M_2)