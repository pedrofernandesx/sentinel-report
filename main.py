import sys
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
sys.path.append(str(BASE_DIR / "src"))

from scanner import get_host_telemetry, scan_ports
from generator import generate_dashboard

def banner():
    print(r"""
   _____            __  _            __ 
  / ___/___  ____  / /_(_)___  ___  / / 
  \__ \/ _ \/ __ \/ __/ / __ \/ _ \/ /  
 ___/ /  __/ / / / /_/ / / / /  __/ /   
/____/\___/_/ /_/\__/_/_/ /_/\___/_/    
    v2.2 :: System Audit Tool
    """)

def main():
    banner()
    
    # Language selector (Default: EN)
    l_opt = input("Language / Idioma [EN/pt]: ").strip().upper()
    lang = "PT" if l_opt in ["PT", "PT-BR", "BR"] else "EN"
    
    try:
        print(f"[*] Initializing telemetry ({lang})...")
        data = get_host_telemetry()
        print(f"    Target: {data['hostname']} ({data['ip_local']})")
        
        print(f"[*] Scanning local ports...")
        open_ports = scan_ports(data['ip_local'])
        
        if open_ports:
            print(f"[+] Open ports: {', '.join(map(str, open_ports))}")
        else:
            print("[-] No common ports exposed.")

        print("[*] Generating HTML dashboard...")
        report = generate_dashboard(data, open_ports, lang)
        print(f"[+] Report saved: {report}\n")

    except KeyboardInterrupt:
        print("\n[!] User aborted.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()