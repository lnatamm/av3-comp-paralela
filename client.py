# Cliente
import socket

HOST = 'localhost'
PORT = 8080

# Cria o socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Conecta ao servidor
    s.connect((HOST, PORT))
    # Envia dados para o servidor
    s.sendall(b"Hello, server!")
    # Recebe dados do servidor
    data = s.recv(1024)
    print(f"Recebido: {data.decode()}")