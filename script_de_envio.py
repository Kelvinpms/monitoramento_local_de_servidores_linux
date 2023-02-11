# import psutil e import requests: São as bibliotecas utilizadas nesse script. A primeira, psutil, é uma biblioteca que permite acessar informações do sistema (CPU, memória, disco, rede, entre outros). A segunda, requests, é uma biblioteca que permite enviar solicitações HTTP. 
import psutil
import requests
# def monitor(): Aqui começa a definição de uma função chamada "monitor".
def monitor():
    # cpu_percent = psutil.cpu_percent() Essa linha utiliza a biblioteca psutil para obter a porcentagem atual de utilização da CPU.
    cpu_percent = psutil.cpu_percent()
    # mem = psutil.virtual_memory() Essa linha utiliza a biblioteca psutil para obter informações sobre a memória virtual do sistema.
    mem = psutil.virtual_memory()
    # mem_total = mem.total Essa linha extrai o valor total da memória do objeto mem.
    mem_total = mem.total
    # mem_available = mem.available Essa linha extrai o valor de memória disponível do objeto mem.
    mem_available = mem.available
    # mem_percent = mem.percent Essa linha extrai a porcentagem de memória em uso do objeto mem.
    mem_percent = mem.percent
    # data = {...} Essa linha cria um dicionário com as informações obtidas da CPU e da memória, que serão enviadas na requisição POST.
    data = {
        "cpu_percent": cpu_percent,
        "mem_total": mem_total,
        "mem_available": mem_available,
        "mem_percent": mem_percent
    }
    # url = "http://127.0.0.1:8000/" Essa linha define a URL da API FastAPI onde os dados serão enviados. No caso, está sendo usada a URL http://127.0.0.1:8000/, que é o endereço local padrão.
    url = "http://127.0.0.1:8000/api/data"
    # response = requests.post(url, json=data) Essa linha envia uma requisição POST para a API FastAPI, com os dados obtidos do sistema em formato JSON.
    response = requests.post(url, json=data)
    # print(response.text) Essa linha imprime a resposta da API FastAPI.
    print(response.text)
# monitor() Essa linha chama a função monitor para executar o código acima.
monitor()
