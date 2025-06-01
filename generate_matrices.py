import numpy as np
import os
# Função para gerar um arquivo de matriz com dimensões n x m 
def generate_matrix_file(filename, n, m):
    # Verifica se o diretório existe, caso contrário, cria
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(f"{n} {m}\n")
        for _ in range(n):
            # Para não ocupar muito espaço, valores fixos, mas você pode gerar aleatórios
            row = ' '.join([str(np.random.randint(1, 10)) for _ in range(m)])
            f.write(row + '\n')

# Gerando arquivos de matrizes de exemplo
generate_matrix_file('matrices/matrix_50x50_a.txt', 50, 50)
generate_matrix_file('matrices/matrix_50x50_b.txt', 50, 50)