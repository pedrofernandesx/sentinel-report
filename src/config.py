# Dicionário de Textos
LANG_TEXT = {
    "EN": {
        "sub": "Infrastructure Audit",
        "id": "ASSET IDENTITY",
        "id_tip": "Unique network fingerprint.",
        "ip": "Private IP",
        "ip_tip": "Local LAN address (RFC 1918). Reachable by internal devices.",
        "load": "RESOURCE USAGE",
        "load_tip": "Hardware metrics.",
        "cpu_tip": "Central Processing Unit. Sustained load > 90% indicates bottlenecks.",
        "ram_tip": "Random Access Memory. Full RAM forces Disk Swap (slow).",
        "disk_tip": "Primary Storage. Low space risks OS stability.",
        "atk": "ATTACK SURFACE",
        "atk_tip": "Listening TCP ports. Closes unused ports to reduce risk.",
        "open": "OPEN",
        "sec": "SECURE",
        "clean": "No critical services exposed.",
        "footer": "SentinelReport Automation • Enterprise Security Tool"
    },
    "PT": {
        "sub": "Auditoria de Infraestrutura",
        "id": "IDENTIDADE DO ATIVO",
        "id_tip": "Impressão digital na rede.",
        "ip": "IP Privado",
        "ip_tip": "Endereço Local (LAN). Acessível por dispositivos na mesma rede.",
        "load": "USO DE RECURSOS",
        "load_tip": "Métricas de hardware.",
        "cpu_tip": "Processador. Carga > 90% indica gargalos ou malware.",
        "ram_tip": "Memória RAM. Se encher, o PC usa o disco (lento).",
        "disk_tip": "Armazenamento. Pouco espaço trava o sistema.",
        "atk": "SUPERFÍCIE DE ATAQUE",
        "atk_tip": "Portas TCP abertas. Feche o que não usa.",
        "open": "ABERTA",
        "sec": "SEGURO",
        "clean": "Nenhum serviço crítico exposto.",
        "footer": "SentinelReport Automation • Ferramenta de Segurança Corporativa"
    }
}

# CSS
CSS_STYLE = """
<style>
    :root { 
        /* Paleta Dark Mode Corporativa */
        --bg: #0f172a;       /* Slate 900 */
        --surface: #1e293b;  /* Slate 800 */
        --text: #f8fafc;     /* Slate 50 */
        --muted: #94a3b8;    /* Slate 400 */
        --border: #334155;   /* Slate 700 */
        
        /* Cores de Status (Sincronizadas com Python) */
        --primary: #3b82f6;  /* Blue 500 */
        --success: #10b981;  /* Emerald 500 (Verde) */
        --warning: #f59e0b;  /* Amber 500 (Laranja/Amarelo) */
        --danger: #ef4444;   /* Red 500 (Vermelho) */
    }

    body { background: var(--bg); color: var(--text); font-family: 'Inter', system-ui, -apple-system, sans-serif; margin: 0; padding: 40px; line-height: 1.6; }
    .container { max-width: 1000px; margin: 0 auto; }
    
    header { border-bottom: 1px solid var(--border); padding-bottom: 20px; margin-bottom: 40px; display: flex; justify-content: space-between; align-items: end; }
    h1 { margin: 0; font-size: 1.6rem; letter-spacing: -0.5px; font-weight: 700; }
    h1 span { color: var(--primary); }
    .meta { color: var(--muted); font-size: 0.85rem; text-align: right; }

    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
    
    /* Cards */
    .card { 
        background: var(--surface); 
        border: 1px solid var(--border); 
        border-radius: 12px; 
        padding: 24px; 
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover { 
        border-color: var(--primary); 
        transform: translateY(-2px); 
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }
    
    .card-head { 
        color: var(--muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;
        margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; 
    }

    /* Metrics Visualization */
    .metric-row { margin-bottom: 16px; }
    
    .metric-label { 
        display: flex; justify-content: space-between; 
        font-size: 0.9rem; margin-bottom: 6px; font-weight: 500; 
    }
    
    .mono { font-family: 'JetBrains Mono', 'Consolas', monospace; font-weight: bold; }
    
    /* Barras de Progresso */
    .bar-bg { 
        background: rgba(255, 255, 255, 0.1); /* Fundo sutil */
        height: 8px; 
        border-radius: 4px; 
        overflow: hidden; 
    }
    .bar-fill { 
        height: 100%; 
        border-radius: 4px; 
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 10px rgba(0,0,0,0.3); /* Brilho suave na barra */
    }

    /* Tooltips & Icons */
    .help-icon {
        cursor: help; width: 18px; height: 18px; border-radius: 50%; border: 1px solid var(--muted);
        color: var(--muted); display: flex; align-items: center; justify-content: center; font-size: 0.7rem;
        transition: all 0.2s;
    }
    .help-icon:hover { color: var(--primary); border-color: var(--primary); background: rgba(59, 130, 246, 0.1); }
    
    .interactive-text { 
        cursor: help; border-bottom: 1px dotted var(--muted); position: relative; transition: color 0.2s;
    }
    .interactive-text:hover { color: var(--text); border-bottom-color: var(--primary); }
    
    .tip { position: relative; }
    .tip:hover::after, .interactive-text:hover::after {
        content: attr(data-msg); position: absolute; bottom: 130%; left: 50%; transform: translateX(-50%);
        background: #020617; border: 1px solid var(--border); color: #fff; padding: 12px; border-radius: 8px;
        font-size: 0.8rem; width: 240px; z-index: 99; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5); 
        text-align: left; line-height: 1.4; font-weight: normal; text-transform: none; letter-spacing: 0; pointer-events: none;
    }

    /* Badges */
    .badge { padding: 4px 10px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.5px; }
    .badge.open { background: rgba(239, 68, 68, 0.15); color: var(--danger); border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge.safe { background: rgba(16, 185, 129, 0.15); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }
    
    footer { margin-top: 60px; text-align: center; color: var(--muted); font-size: 0.8rem; border-top: 1px solid var(--border); padding-top: 20px; }
</style>
"""