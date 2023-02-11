
import psutil
import requests

def monitor():
    
    cpu_percent = psutil.cpu_percent()

    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_available = mem.available
    mem_percent = mem.percent

    data = {
        "cpu_percent": cpu_percent,
        "mem_total": mem_total,
        "mem_available": mem_available,
        "mem_percent": mem_percent
    }
    url = "http://127.0.0.1:8000/"
    response = requests.post(url, json=data)
    print(response.text)

monitor()
