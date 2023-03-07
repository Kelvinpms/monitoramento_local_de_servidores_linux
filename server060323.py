import psutil
import time
import platform
import uuid
import json
from datetime import datetime, timezone
import requests
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(level=logging.INFO, filename="registro.log", format="%(asctime)s - %(levelname)s - %(message)s")

auth = HTTPBasicAuth('ServerName', 'ServerPassword')

url = 'http://187.127.61.63/api'

try:       
    request = requests.request('GET', url + '/Server/188.211.160.231', auth=auth) 
    print(request.status_code)
    todos = json.loads(request.content)
    logging.info(f"Conexao estabelecida com a API")
    dados = request.json()

except:
    print("Erro ao acessar a API")  
    logging.error(f"Erro ao acessar a API")
    todos = {}

logging.info(f"Dados do servidor: {todos}")

machine_id = todos.get('machineId')
nome = todos.get('name')
ip_server = todos.get('ipAddress')
desc = todos.get('description')
creation_date = todos.get('creationDate')
deactivation_date = todos.get('deactivationDate')

machine_uuid = str(machine_id)
ip = str(ip_server)
mt_date = datetime.now()
monitoring_date = str(mt_date)

data_services = {"data_services": []}
partitions = psutil.disk_partitions()
for partition in partitions:
    dev = partition.device
    caption = str(dev)

    monted_on = partition.mountpoint
    monted = str(monted_on)

    partition_usage = psutil.disk_usage(partition.mountpoint)

    total = partition_usage.total
    size = str(total)

    free_space = partition_usage.free
    free = str(free_space)

    service_data = {
        "caption": caption,
        "mountedOn": monted,
        "size": size,
        "freeSpace": free
    }
    data_services["data_services"].append(service_data)

monitor_id = uuid.uuid4()
monitoring_uuid = str(monitor_id)
cpu_count = psutil.cpu_count()
load_perc = psutil.cpu_percent()
load_percentage = int(load_perc)
mem = psutil.virtual_memory()
mem_size = mem.total
mem_physical = mem.available
disk_partitions = psutil.disk_partitions()

data = {
  "machineId": machine_id,
  "name": nome,
  "description": desc,
  "ipAddress": ip_server,
  "creationDate": creation_date,
  "deactivationDate": deactivation_date,
    "active": True,
    "monitor": True,
    "useCredential": False,
    "type": 1,
    "monitoringParameters": {
    "lowCpuAlert": 90,
    "mediumCpuAlert": 95,
    "highCpuAlert": 98,
    "mediumCpuAlert": 95,
    "highCpuAlert": 98,
    "lowMemoryAlert": 90,
    "mediumMemoryAlert": 95,
    "highMemoryAlert": 98,
    "lowDiskSpaceAlert": 90,
    "mediumDiskSpaceAlert": 95,
    "highDiskSpaceAlert": 98
    },
    "monitorings": [
    {
    "monitoringId": monitoring_uuid,
    "monitoringDate": monitoring_date,
    "machineId": machine_uuid,
    "numberOfLogicalProcessors": cpu_count,
    "loadPercentage": load_percentage,
    "numberOfCores": 1,
    "lastBootUpTime": "2023-03-01T14:01:36.234Z",
    "enableDaylightSavingsTime": True,
    "osVersion": platform.version(),
    "ipAddress": ip,
    "memory": {
    "totalVisibleMemorySize": mem_size,
    "freePhysicalMemory": mem_physical
    },
    "drives": data_services["data_services"],
    "services": []
    }
    ]
    }

try:
    response = requests.post(url + '/Monitor/Dados', json=data, auth=auth)
    print(response.status_code)
    logging.info("Conexão estabelecida para envio dos dados")
    print(response.text)
except:
    print("Erro ao enviar dados")
    logging.error("Erro ao enviar dados para a API")  
