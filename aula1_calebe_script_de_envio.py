import requests
import json

# Define a URL da API que você deseja acessar
url = "https://exemplo.com/api"

# Define o caminho para o arquivo JSON que deseja enviar
arquivo_json = "/path/para/arquivo.json"

# Define as informações do cabeçalho da requisição
headers = {
    "Host": "exemplo.com",
    "User-Agent": "Seu user-agent aqui",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Authorization": "Seu token de autorização aqui"
}

# Lê o arquivo JSON e armazena seu conteúdo em uma variável
with open(arquivo_json) as arquivo:
    conteudo_json = json.load(arquivo)

# Envia uma solicitação POST para a API com o conteúdo JSON definido e as informações do cabeçalho
response = requests.post(url, json=conteudo_json, headers=headers)

# Verifica se a solicitação foi bem sucedida
if response.status_code == 200:
    # Se a solicitação foi bem sucedida, imprime a resposta da API
    print(response.json())
else:
    # Se a solicitação falhou, imprime uma mensagem de erro com o código de status da resposta
    print("Erro ao fazer solicitação. Código de status: " + str(response.status_code))
