import socket

class Server:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print(f"Servidor iniciado em {self.host}:{self.port}")

        while True:
            conn, addr = self.socket.accept()
            print(f"Conectado por {addr}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Recebido: {data.decode()}")
                    # Processa os dados recebidos
                    vector_x, vector_y = data.decode().split(';')
                    result = self.__multiply_vectors(vector_x, vector_y)
                    conn.sendall("Vetores recebidos!".encode())

    def stop(self):
        self.socket.close()
        print("Servidor parado")

    def __multiply_vectors(self, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            raise ValueError("Vectors must be of the same length")
        result = []
        for x, y in zip(self.vector_x, self.vector_y):
            result.append(x * y)
        return result