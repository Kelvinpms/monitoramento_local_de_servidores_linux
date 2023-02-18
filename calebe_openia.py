import openai
import os

openai.api_key = "sua_chave_api_da_openai"

# Define os arquivos que serão usados para treinar o modelo
files = [
    'caminho/do/arquivo1.json',
    'caminho/do/arquivo2.json'
]

# Define os parâmetros de treinamento
model = "text-babbage-001"
fine_tune_params = {
    'model': model,
    'files': files,
    'epochs': 3,
    'learning_rate': 5e-5
}

# Inicia o treinamento
response = openai.FineTune.create(**fine_tune_params)

# Obtém o ID do modelo treinado
model_id = response['model']
print(f"Modelo treinado com ID: {model_id}")
