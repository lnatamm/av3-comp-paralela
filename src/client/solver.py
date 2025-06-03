import threading
import socket

class Solver:
    def __init__(self, servers=[('localhost', 8080), ('localhost', 8081)], number_of_retries=5):
        self.servers = servers
        self.number_of_retries = number_of_retries
        self.lock = threading.Lock()
        self.server_index = 0

    # Método para obter o próximo servidor da lista de servidores
    def __get_next_server(self):
        # Usa um lock para garantir que o acesso ao índice do servidor seja thread-safe
        with self.lock:
            server = self.servers[self.server_index]
            self.server_index = (self.server_index + 1) % len(self.servers)
            return server
        
    def send_vectors_to_server(self, vector_x, vector_y):
        # Validação dos vetores
        if len(vector_x) != len(vector_y):
            raise ValueError("Vectors must be of the same length")
        
        # Converte os vetores para o formato de string para envio
        vector_x_str = self.__stringfy_vector(vector_x)
        vector_y_str = self.__stringfy_vector(vector_y)
        
        # Envia a mensagem com os vetores para o servidor resolver
        message = f"{vector_x_str};{vector_y_str}"

        retries = 0
        while retries < self.number_of_retries:
            # Pega um servidor diferente a cada chamada
            host, port = self.__get_next_server()
            try:
                # Criar socket temporário para esta thread
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((host, port))
                    sock.sendall(message.encode())

                    # Recebe a resposta do servidor
                    print("Waiting for response from server...")
                    data = sock.recv(1024)

                    # Caso receba dados, converte a resposta recebida do servidor de volta para um número float
                    if data:
                        response = float(data.decode())
                        print(f"Response from server ({host}:{port}): {response}")
                        return response
                    
                    # Se não receber dados, tenta novamente até o número máximo de tentativas
                    else:
                        print(f"Retry {retries}/{self.number_of_retries}: No data received from server, raising exception.")
                        print("Exception occurred during multiplication of vectors: ")
                        print(f"Vector X: {vector_x}, Vector Y: {vector_y}")
                        raise Exception("No data received from server after multiple retries.")

            except Exception as e:
                print(f"[{host}:{port}] Tentativa {retries+1} falhou: {e}")
                retries += 1

        # Se não receber dados após o número máximo de tentativas, levanta uma exceção
        raise Exception("Failed to connect to any server after multiple retries.")

        

    def __stringfy_vector(self, vector):
        """Converts a vector to a string format for sending."""
        return ','.join(map(str, vector))

    def multiply_matrices(self, M_1, M_2):

        # Armazena as dimensões das matrizes M_1 e M_2
        n_1, m_1 = len(M_1), len(M_1[0])
        n_2, m_2 = len(M_2), len(M_2[0])
        
        # Verifica se as dimensões das matrizes são compatíveis para multiplicação
        if m_1 != n_2:
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second matrix")
        
        # Inicializa a matriz de resultados com zeros
        results = [[0] * m_2 for _ in range(n_1)]
        # Cria uma lista de threads para realizar a multiplicação de forma concorrente
        threads = []

        # Função que será executada por cada thread para enviar os vetores ao servidor e anotar o resultado na matriz de resultados
        def worker(i, j, vector_x, vector_y):
            result = self.send_vectors_to_server(vector_x, vector_y)
            results[i][j] = result

        for i in range(n_1):
            # Para cada linha da primeira matriz, pega o vetor correspondente
            vector_x = M_1[i]
            for j in range(m_2):
                # Para cada coluna da segunda matriz, pega o vetor correspondente
                vector_y = [M_2[k][j] for k in range(n_2)]
                # Cria uma nova thread para enviar os vetores ao servidor e armazenar o resultado
                t = threading.Thread(target=worker, args=(i, j, vector_x, vector_y))
                # Inicia a thread
                t.start()
                # Adiciona a thread à lista de threads para posteriormente aguardar sua conclusão
                threads.append(t)

        # Aguarda todas as threads terminarem
        for t in threads:
            # Esse método bloqueia a execução até que a thread termine
            t.join()

        # Retorna a matriz de resultados após todas as threads terem completado a multiplicação
        return results