# 🧠 Multiplicação de Matrizes com Threads e Sockets

Este projeto implementa uma solução distribuída para multiplicação de matrizes usando **threads** no cliente e **sockets TCP** para comunicação com um servidor. Cada multiplicação escalar entre uma linha e uma coluna é enviada como tarefa para o servidor, que realiza o cálculo e retorna o resultado ao cliente.

## ⚙️ Requisitos

- Python 3.7+
- Biblioteca `numpy` (somente para geração de matrizes)

Instale com:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como executar

### 1. Inicie o servidor

Abra um terminal na raiz do projeto e execute:

```bash
python .\src\server\server.py
```

Isso iniciará o servidor na porta `8080`, aguardando requisições de multiplicação escalar.

### 2. Execute o cliente

Em outro terminal, rode o cliente para realizar a multiplicação de duas matrizes:

```bash
python .\main.py  
```

Esse script irá:

- Ler duas matrizes do diretório `matrices/`.
- Enviar os produtos escalares linha × coluna para o servidor.
- Imprimir a matriz resultante e o tempo de execução.

---

## 🛠️ Gerar Matrizes Personalizadas

Você pode gerar matrizes de qualquer tamanho com o script `generate_matrices.py`:

```python
# Exemplo no final do arquivo:
generate_matrix_file('matrices/matrix_100x60_a.txt', 100, 60)
generate_matrix_file('matrices/matrix_60x100_b.txt', 60, 100)
```

Execute com:

```bash
python .\generate_matrices.py
```

---

## 📌 Detalhes Técnicos

- A classe `Solver` (em `solver.py`) cria uma thread para cada multiplicação escalar necessária.
- Cada thread se comunica com o servidor enviando pares de vetores (linha × coluna).
- O servidor realiza o produto escalar e retorna o resultado ao cliente.
- Comunicação via sockets (`socket.AF_INET`, `socket.SOCK_STREAM`).
- Execução paralela via `threading.Thread`.

---

## 📄 Detalhes do Projeto

Os detalhes completos do projeto podem ser encontrados no arquivo [`TRABALHO COMPUTAÇÃO PARALELA CONCORRENTE AV3.pdf`](TRABALHO_COMPUTAÇÃO_PARALELA_CONCORRENTE_AV3.pdf).

---

## 🧪 Exemplo de Saída

```text
Resultado da multiplicação:
[140.0, 133.0, 147.0, ...]
[117.0, 129.0, 122.0, ...]
...
Tempo de execução paralelo: 0.45 segundos
```

---

## 👥 Autores

### **Levi Natã Monteiro Maciel** – 6º semestre de Ciência da Computação – UNIFOR  
### **João Victor Leles Cordeito** – 6º semestre de Ciência da Computação – UNIFOR