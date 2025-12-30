import os
from datetime import datetime

def create_html_report(sys_data, open_ports):
    """Gera um Dashboard HTML Cyberpunk com explicações didáticas e barras visuais."""
    
    # Lógica de Cores para as Barras de Progresso
    def get_color(value):
        if value < 50: return "#00ff41"  # Verde (Safe)
        if value < 80: return "#fdf500"  # Amarelo (Warning)
        return "#ff003c"                 # Vermelho (Danger)

    cpu_color = get_color(sys_data['cpu_uso'])
    ram_color = get_color(sys_data['memoria_uso'])
    disk_color = get_color(sys_data['disco_uso'])

    # CSS Injetado 
    css_style = """
    <style>
        :root {
            --bg-color: #050505;
            --card-bg: #111;
            --neon-green: #00ff41;
            --neon-purple: #9d00ff;
            --neon-red: #ff003c;
            --text-main: #e0e0e0;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: 'Consolas', 'Courier New', monospace;
            margin: 0; padding: 20px;
            background-image: radial-gradient(circle, #1a1a1a 1px, transparent 1px);
            background-size: 30px 30px; /* Efeito de Grid no fundo */
        }
        .container { max-width: 1000px; margin: 0 auto; }
        
        /* CABEÇALHO */
        header {
            text-align: center;
            border-bottom: 2px solid var(--neon-purple);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        h1 { margin: 0; color: var(--neon-green); text-shadow: 0 0 10px var(--neon-green); letter-spacing: 3px; }
        .subtitle { color: var(--neon-purple); font-size: 0.9em; opacity: 0.8; }

        /* GRID LAYOUT */
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        /* CARDS */
        .card {
            background: var(--card-bg);
            border: 1px solid #333;
            border-left: 4px solid var(--neon-purple);
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
            transition: transform 0.2s;
        }
        .card:hover { transform: translateY(-3px); border-left-color: var(--neon-green); }
        h2 { color: var(--neon-purple); border-bottom: 1px dashed #444; padding-bottom: 10px; margin-top: 0; display: flex; align-items: center; justify-content: space-between; }
        
        /* BARRAS DE PROGRESSO */
        .progress-container {
            background: #222;
            height: 10px;
            width: 100%;
            border-radius: 5px;
            margin-top: 5px;
            overflow: hidden;
        }
        .progress-bar { height: 100%; transition: width 0.5s; }
        .stat-row { margin-bottom: 15px; }
        .stat-label { display: flex; justify-content: space-between; font-size: 0.9em; font-weight: bold; }

        /* LISTA DE PORTAS */
        ul { list-style: none; padding: 0; }
        li { padding: 8px; border-bottom: 1px solid #222; display: flex; align-items: center; }
        li::before { content: "►"; color: var(--neon-green); margin-right: 10px; font-size: 0.8em; }
        .port-open { color: var(--neon-red); font-weight: bold; }
        .port-safe { color: #888; font-style: italic; }

        /* TOOLTIPS (A Mágica da Explicação) */
        .tooltip {
            position: relative;
            cursor: help;
            border-bottom: 1px dotted var(--neon-green);
        }
        .tooltip::after {
            content: attr(data-tip);
            position: absolute;
            bottom: 125%; left: 50%; transform: translateX(-50%);
            background: #222; border: 1px solid var(--neon-green);
            color: #fff; padding: 8px; border-radius: 4px;
            font-size: 0.8em; width: 220px;
            visibility: hidden; opacity: 0;
            transition: opacity 0.3s;
            z-index: 10; text-align: center;
            box-shadow: 0 0 10px rgba(0,255,65,0.2);
        }
        .tooltip:hover::after { visibility: visible; opacity: 1; }

        footer { text-align: center; margin-top: 40px; color: #555; font-size: 0.8em; }
    </style>
    """

    # HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>SENTINEL REPORT v2.0</title>
        {css_style}
    </head>
    <body>
        <div class="container">
            <header>
                <h1>💀 SENTINEL REPORT</h1>
                <div class="subtitle">AUDITORIA DE SISTEMA AUTOMATIZADA // {datetime.now().strftime("%d/%m/%Y %H:%M")}</div>
            </header>
            
            <div class="dashboard">
                
                <!-- CARD 1: IDENTIDADE -->
                <div class="card">
                    <h2>🖥️ ALVO <span style="font-size:0.6em; cursor:help" title="Informações básicas de identificação da máquina">?</span></h2>
                    <p><strong>HOSTNAME:</strong> {sys_data['hostname']}</p>
                    <p><strong>IP LOCAL:</strong> <span class="tooltip" data-tip="Endereço interno na sua rede local. Não é seu IP público de internet.">{sys_data['ip_local']}</span></p>
                    <p><strong>SISTEMA:</strong> {sys_data['sistema']}</p>
                    <p><strong>BOOT:</strong> {sys_data['boot_time']}</p>
                </div>

                <!-- CARD 2: RECURSOS (Com Barras Visuais) -->
                <div class="card">
                    <h2>⚡ RECURSOS <span style="font-size:0.6em; cursor:help" title="Monitoramento de carga de hardware">?</span></h2>
                    
                    <div class="stat-row">
                        <div class="stat-label">
                            <span class="tooltip" data-tip="Processador: O cérebro do PC. Acima de 80% constante pode indicar lentidão ou malware.">CPU</span>
                            <span style="color:{cpu_color}">{sys_data['cpu_uso']}%</span>
                        </div>
                        <div class="progress-container"><div class="progress-bar" style="width:{sys_data['cpu_uso']}%; background:{cpu_color}"></div></div>
                    </div>

                    <div class="stat-row">
                        <div class="stat-label">
                            <span class="tooltip" data-tip="Memória RAM: Onde os programas rodam. Se encher, o PC trava.">RAM</span>
                            <span style="color:{ram_color}">{sys_data['memoria_uso']}%</span>
                        </div>
                        <div class="progress-container"><div class="progress-bar" style="width:{sys_data['memoria_uso']}%; background:{ram_color}"></div></div>
                        <small style="color:#666">Total: {sys_data['memoria_total']}</small>
                    </div>

                    <div class="stat-row">
                        <div class="stat-label">
                            <span class="tooltip" data-tip="Armazenamento principal.">DISCO (C:)</span>
                            <span style="color:{disk_color}">{sys_data['disco_uso']}%</span>
                        </div>
                        <div class="progress-container"><div class="progress-bar" style="width:{sys_data['disco_uso']}%; background:{disk_color}"></div></div>
                    </div>
                </div>

                <!-- CARD 3: REDE -->
                <div class="card">
                    <h2>🌐 REDE & SEGURANÇA <span style="font-size:0.6em; cursor:help" title="Pontos de entrada potenciais para invasores">?</span></h2>
                    <p style="font-size:0.9em; color:#aaa; margin-bottom:15px;">
                        Portas são "portões" digitais. Portas abertas desnecessárias são riscos de segurança.
                    </p>
                    <ul>
                        {''.join([f"<li><span class='port-open'>🔓 PORTA {p} ABERTA</span> <span class='tooltip' data-tip='Serviço comum rodando nesta porta. Verifique se você realmente precisa dele.'>[?]</span></li>" for p in open_ports]) or "<li class='port-safe'>🔒 Nenhuma porta crítica detectada no scan rápido.</li>"}
                    </ul>
                </div>

            </div> <!-- Fim Dashboard -->

            <footer>
                SENTINEL SYSTEM v2.0 | GERADO POR PYTHON | SECURITY BY DESIGN
            </footer>
        </div>
    </body>
    </html>
    """
    
    output_path = os.path.join("output", "relatorio_sentinel.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return output_path