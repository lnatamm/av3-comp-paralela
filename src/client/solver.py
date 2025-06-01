class Solver:
    def __init__(self):
        pass

    def send_vectors_to_server(self, vector_x, vector_y):
        pass

    def multiply_matrices(self, M_1, M_2):
        n_1, m_1 = len(M_1), len(M_1[0])
        n_2, m_2 = len(M_2), len(M_2[0])
        if m_1 != n_2:
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second matrix")
        
        results = []

        for i in range(n_1):
            vector_x = M_1[i]
            for j in range(m_2):
                vector_y = [M_2[k][j] for k in range(n_2)]
                # TODO: Send both vectors to the server for multiplication
                results.append(self.send_vectors_to_server(vector_x, vector_y))

        product = []
        for i in range(n_1):
            product.append([0] * m_2)

        #TODO: Mount the results


    # Cliente
    # import socket

    # HOST = 'localhost'
    # PORT = 8080

    # # Cria o socket
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     # Conecta ao servidor
    #     s.connect((HOST, PORT))
    #     # Envia dados para o servidor
    #     s.sendall(b"Hello, server!")
    #     # Recebe dados do servidor
    #     data = s.recv(1024)
    #     print(f"Recebido: {data.decode()}")