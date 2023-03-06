import psutil
import time
import platform
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('', '')

contador = 1
while True:
    cpu_count = psutil.cpu_count()
    cpu_load_percent = psutil.cpu_percent(interval=1, percpu=True)
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_available = mem.available
    disk_partitions = psutil.disk_partitions()
    disk_usage = {
        partition.device: psutil.disk_usage(partition.mountpoint)._asdict()
        for partition in disk_partitions
    }
    data_services = {
        "data_services": []
    }
    services = psutil.win_service_iter()
    for service in services:
        service_data = {
            "name": service.name(),
            "display_name": service.display_name(),
            "status": service.status()
            # adicione outras informações que você precisar
        }
        data_services["data_services"].append(service_data)
    
    data = {
        "monitoring_id": contador,
        "machine_id": "my_machine",
        "number_of_logical_processors": cpu_count,
        "load_percentage": cpu_load_percent[-1],
        "number_of_cores": psutil.cpu_count(logical=False),
        "last_boot_time": psutil.boot_time(),
        "enable_daylight_savings_time": time.localtime().tm_isdst,
        "total_visible_memory_size": mem_total,
        "free_physical_memory": mem_available,
        "drives": disk_usage,
        "services": data_services,
        "monitoring_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "ip_address": psutil.net_if_addrs()["Ethernet"][1].address,
        "os_version": platform.platform(),
    }
    url = ""
    try:
        response1 = requests.get(url, json=data, auth=auth)
        print(response1.text)
    except:
        print("get erro") 
    try:       
        response = requests.post(url, json=data, auth=auth)
        print(response.text)
    except:
        print("post erro")    
    contador += 1
    input()
