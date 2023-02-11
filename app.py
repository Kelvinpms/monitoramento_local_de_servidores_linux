#uvicorn app:app --reload
from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/system_info")
def system_info():
    cpu_percent = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_available = mem.available
    mem_percent = mem.percent
    return {
        "cpu_percent": cpu_percent,
        "mem_total": mem_total,
        "mem_available": mem_available,
        "mem_percent": mem_percent
    }
