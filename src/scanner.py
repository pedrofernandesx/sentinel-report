import socket
import platform
import psutil
import datetime
from typing import Dict, List, Any

def get_host_telemetry() -> Dict[str, Any]:
    boot_ts = psutil.boot_time()
    
    return {
        "hostname": socket.gethostname(),
        "ip_local": _get_lhost(),
        "os_version": f"{platform.system()} {platform.release()}",
        "boot_time": datetime.datetime.fromtimestamp(boot_ts).strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_load": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent,
        "ram_total": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        "disk_usage": psutil.disk_usage('/').percent
    }

def _get_lhost() -> str:
    # UDP connect trick to get the real interface IP without sending data
    # Truque de conexão UDP para obter o IP real da interface sem enviar dados
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("1.1.1.1", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

def scan_ports(target: str, ports: List[int] = None) -> List[int]:
    # Common attack vectors
    if not ports:
        ports = [21, 22, 23, 80, 443, 3306, 3389, 5432, 8080]
    
    open_ports = []
    socket.setdefaulttimeout(0.3) # Aggressive timeout for LAN speed
    
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
                
    return open_ports