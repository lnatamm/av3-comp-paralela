import socket
import threading

class Server:
    def __init__(self, host='localhost', port=8081):
        self.host = host
        self.port = port
        # Cria um socket utilizando o protocolo IPv4 (AF_INET) e TCP (SOCK_STREAM)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        if hasattr(self, 'socket'):
            self.stop()

    def start(self):
        # Permite reutilizar o endereço do socket mesmo que ele ainda esteja em uso
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Associa o socket ao endereço e porta especificados
        self.socket.bind((self.host, self.port))
        # Coloca o socket em modo de escuta, permitindo conexões
        self.socket.listen()
        print(f"Servidor iniciado em {self.host}:{self.port}")

        # Loop para aceitar conexões de clientes continuamente
        while True:
            # Aguarda e aceita uma conexão de um cliente
            conn, addr = self.socket.accept()
            print(f"Conectado por {addr}")
            # Cria uma nova thread para lidar com o cliente, dessa forma o servidor pode atender múltiplos clientes simultaneamente
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            # Inicia a thread
            thread.start()

    # Método para lidar com a conexão de um cliente
    def handle_client(self, conn, addr):
        with conn:
            try:
                # Recebe dados do cliente
                data = conn.recv(1024)
                if not data:
                    return
                print(f"Recebido de {addr}: {data.decode()}")

                # Desempacota os vetores recebidos
                vector_x_str, vector_y_str = data.decode().split(';')
                # Converte as strings em vetores de float
                vector_x = self.__convert_response_to_vector(vector_x_str)
                vector_y = self.__convert_response_to_vector(vector_y_str)

                print(f"Vetores recebidos: {vector_x}, {vector_y}")
                # Realiza a multiplicação dos vetores
                result = self.__multiply_vectors(vector_x, vector_y)
                print(f"Resultado da multiplicação: {result}")

                # Envia o resultado de volta para o cliente
                conn.sendall(str(result).encode())
                print(f"Resultado enviado para {addr}: {result}")

            except Exception as e:
                print(f"Erro com {addr}: {e}")

    def stop(self):
        self.socket.close()
        print("Socket fechado.")

    def __convert_response_to_vector(self, response):
        return list(map(float, response.split(',')))

    def __multiply_vectors(self, vector_x, vector_y):
        if len(vector_x) != len(vector_y):
            raise ValueError("Vectors must be of the same length")
        # Multiplicação escalar (produto interno) entre os vetores
        sum = 0
        for x, y in zip(vector_x, vector_y):
            sum += x * y
        return sum
    
if __name__ == "__main__":
    server = Server()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
        server.stop()
    except Exception as e:
        print(f"Erro: {e}")
        server.stop()
