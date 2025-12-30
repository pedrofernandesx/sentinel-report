import socket
import platform
import psutil
import datetime

def get_system_info():
    """Coleta informações vitais do sistema operacional e hardware."""
    try:
        info = {
            "sistema": f"{platform.system()} {platform.release()}",
            "hostname": socket.gethostname(),
            "ip_local": get_local_ip(),
            "cpu_uso": psutil.cpu_percent(interval=1),
            "memoria_total": f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
            "memoria_uso": psutil.virtual_memory().percent,
            "disco_uso": psutil.disk_usage('/').percent,
            "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        }
        return info
    except Exception as e:
        return {"erro": str(e)}

def get_local_ip():
    """Pega o IP local de forma robusta (evita retornar 127.0.0.1 sempre)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) # Tenta conectar no Google (sem enviar dados)
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def scan_ports(target_ip, ports=[21, 22, 80, 443, 3306, 8080]):
    """Verifica quais portas da lista estão abertas no alvo."""
    open_ports = []
    # Timeout baixo pra ser rápido (mas pode perder precisão em redes lentas)
    socket.setdefaulttimeout(0.5) 
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target_ip, port)) # Retorna 0 se sucesso
        if result == 0:
            open_ports.append(port)
        s.close()
    
    return open_ports