#uvicorn app:app --reload
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class DataInput(BaseModel):
    cpu_percent: float
    mem_total: float
    mem_available: float
    mem_percent: float
@app.post("/api/data")
async def receive_data(data: DataInput):
    cpu_percent = data.cpu_percent
    mem_total = data.mem_total
    mem_available = data.mem_available
    mem_percent = data.mem_percent

    # Faça o processamento desejado com os dados recebidos

    return {"cpu_percent": cpu_percent, "mem_total": mem_total, "mem_available": mem_available, "mem_percent": mem_percent}

