import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from scanner import get_system_info, scan_ports
from generator import create_html_report

def main():
    print("\n" + "="*40)
    print("💀 SENTINEL REPORT - INICIANDO VARREDURA")
    print("="*40)
    
    # 1. Coleta dados do sistema
    print("[*] Coletando dados do sistema...", end=" ")
    sys_info = get_system_info()
    print("OK")
    
    # 2. Scaneia portas (usa o próprio IP local)
    target = sys_info['ip_local']
    print(f"[*] Escaneando portas no alvo {target}...", end=" ")
    open_ports = scan_ports(target)
    print(f"Encontradas: {len(open_ports)}")
    
    # 3. Gera o relatório
    print("[*] Gerando relatório HTML...", end=" ")
    path = create_html_report(sys_info, open_ports)
    print("OK")
    
    print("="*40)
    print(f"✅ SUCESSO! Relatório salvo em:\n{os.path.abspath(path)}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()