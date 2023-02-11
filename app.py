# Use esse comando para iniciar a api "uvicorn app:app --reload"
#################
#from fastapi import FastAPI: Essa linha importa a classe FastAPI da biblioteca FastAPI, que será usada para criar a nossa API.
from fastapi import FastAPI
#from pydantic import BaseModel: Essa linha importa a classe BaseModel da biblioteca Pydantic, que será usada para definir o modelo de dados que será enviado para a nossa API.
from pydantic import BaseModel
# app = FastAPI(): Essa linha cria uma instância da classe FastAPI chamada app, que será usada para definir as rotas da nossa API.
app = FastAPI()
# class DataInput(BaseModel): Essa linha define a classe DataInput como uma subclasse de BaseModel. Isso permite definir as propriedades dos dados de entrada que serão recebidos pela nossa API.
class DataInput(BaseModel):
    # cpu_percent: float, mem_total: float, mem_available: float, mem_percent: float: Essas são as propriedades dos dados de entrada definidos na classe DataInput. Cada propriedade é uma variável que representa um valor de ponto flutuante.
    cpu_percent: float    
    mem_total: float
    mem_available: float
    mem_percent: float
 #@app.post("/api/data"): Essa é uma anotação que define a rota que será usada para receber os dados. Neste caso, é uma rota POST em /api/data.       
@app.post("/api/data")
#async def receive_data(data: DataInput):: Essa linha define a função que será executada quando a rota /api/data for chamada com um pedido POST. A função é assíncrona, o que significa que pode lidar com várias solicitações ao mesmo tempo. O parâmetro data é um objeto do tipo DataInput, que representa os dados que foram enviados para a nossa API.
async def receive_data(data: DataInput):
    # cpu_percent = data.cpu_percent, mem_total = data.mem_total, mem_available = data.mem_available, mem_percent = data.mem_percent: Essas linhas extraem os valores das propriedades dos dados de entrada e armazenam esses valores em variáveis separadas. Isso torna mais fácil trabalhar com esses dados.
    cpu_percent = data.cpu_percent
    mem_total = data.mem_total
    mem_available = data.mem_available
    mem_percent = data.mem_percent

    #return {"cpu_percent": cpu_percent, "mem_total": mem_total, "mem_available": mem_available, "mem_percent": mem_percent}: Essa linha retorna um objeto JSON que contém as mesmas propriedades dos dados de entrada. Isso significa que estamos retornando os mesmos dados que foram enviados para a nossa API, mas em um formato mais fácil de ler e processar. Esses dados podem ser usados para processamento adicional na nossa aplicação.

    return {"cpu_percent": cpu_percent, "mem_total": mem_total, "mem_available": mem_available, "mem_percent": mem_percent}

