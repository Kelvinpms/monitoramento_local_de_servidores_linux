import openai
import os

# Configuração da API key
openai.api_key = "sua_api_key_aqui"

# Carrega dados de treinamento de um arquivo local
with open("seu_arquivo_de_treinamento.json", "r") as f:
    training_data = f.read()

# Define os parâmetros do fine-tuning
model = "text-davinci-002"
fine_tune_params = {
    "model": model,
    "train": training_data,
    "prompt": "Seu prompt aqui",
    "temperature": 0.5,
    "max_tokens": 1024,
    "n_epochs": 3,
    "batch_size": 32
}

# Executa o fine-tuning
response = openai.FineTune.create(**fine_tune_params)

# Salva o modelo treinado em um arquivo local
model_id = response.model.id
model_path = os.path.join("modelos", f"{model_id}.tar.gz")
response.model.save(model_path)
