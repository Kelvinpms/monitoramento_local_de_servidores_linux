import psycopg2
import psutil
def monitor():
    # Conectando ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        host="10.154.211.57S",
        database="server_monitor",
        user="postgres",
        password="postgres"
    )
    # Criando cursor para realizar consultas no banco de dados
    cur = conn.cursor()
    # Obtendo informações de CPU
    cpu_percent = psutil.cpu_percent()
    # Obtendo informações de memória
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_available = mem.available
    mem_percent = mem.percent
    # Inserindo informações de CPU e memória no banco de dados
    cur.execute("INSERT INTO server_monitor (cpu_percent, mem_total, mem_available, mem_percent) VALUES (%s, %s, %s, %s)",
                (cpu_percent, mem_total, mem_available, mem_percent))
    conn.commit()
    # Consultando informações no banco de dados
    cur.execute("SELECT * FROM server_monitor")
    result = cur.fetchall()
    # Exibindo informações na tela
    print("Informações de CPU, memória e dados do servidor:")
    for row in result:
        print("CPU: ", row[1], "%")
        print("Memória total: ", row[2], "bytes")
        print("Memória disponível: ", row[3], "bytes")
        print("Uso de memória: ", row[4], "%")
    # Fechando conexão com o banco de dados
    cur.close()
    conn.close()
# Executando monitoramento
monitor()
