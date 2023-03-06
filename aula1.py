import requests
import psycopg2
import json

# Endereço da API REST
url = ''

# Envia uma solicitação GET à API e armazena a resposta em uma variável
response = requests.get(url)

# Converte a resposta da API em um dicionário Python
data = json.loads(response.text)

# Conecta-se ao banco de dados PostgreSQL
conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password=""
)

# Cria um cursor para executar comandos no banco de dados
cursor = conn.cursor()

# Insere os dados do dicionário em uma tabela no banco de dados
cursor.execute("INSERT INTO monitoring (monitoring_id, monitor_id, total, mem_available, mem_percent) VALUES (%s, %s, %s, %s, %s)", (data['monitoring_id'], data['monitor_id'], data['total'], data['mem_available'], data['mem_percent']))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
