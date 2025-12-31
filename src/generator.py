import os
from datetime import datetime
from typing import Dict, List
# Importamos as configurações do arquivo vizinho
from config import LANG_TEXT, CSS_STYLE

def generate_dashboard(ctx: Dict, ports: List[int], lang: str = "EN") -> str:
    # Busca o texto no config.py
    t = LANG_TEXT.get(lang, LANG_TEXT["EN"])

    def _color(val):
        return "#10b981" if val < 60 else "#f59e0b" if val < 85 else "#ef4444"

    c_cpu = _color(ctx['cpu_load'])
    c_ram = _color(ctx['ram_usage'])
    c_dsk = _color(ctx['disk_usage'])

    if ports:
        ports_html = "".join([
            f"<div style='padding:12px 0; border-bottom:1px solid #334155; display:flex; align-items:center; justify-content:space-between;'>"
            f"<span class='mono'>PORT {p}</span> <span class='badge open'>{t['open']}</span></div>" 
            for p in ports
        ])
    else:
        ports_html = f"<div style='padding:15px 0; display:flex; align-items:center; gap:10px;'><span class='badge safe'>{t['sec']}</span> <span style='color:var(--muted); font-size:0.9rem'>{t['clean']}</span></div>"

    # CSS_STYLE import
    html = f"""
    <!DOCTYPE html>
    <html lang="{lang.lower()}">
    <head><meta charset="UTF-8"><title>Sentinel Report</title>{CSS_STYLE}</head>
    <body>
        <div class="container">
            <header>
                <div><h1>Sentinel<span>Report</span></h1><div style="color:var(--muted); font-size:0.9rem">{t['sub']}</div></div>
                <div class="meta">TARGET: {ctx['hostname']}<br>{datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
            </header>
            <div class="grid">
                
                <!-- Identity -->
                <div class="card">
                    <div class="card-head">{t['id']} <div class="tip help-icon" data-msg="{t['id_tip']}">?</div></div>
                    <div class="metric-row"><div>Hostname</div><div class="mono" style="color:var(--text)">{ctx['hostname']}</div></div>
                    <div class="metric-row">
                        <div style="display:flex; align-items:center; gap:5px;">
                            <span class="interactive-text" data-msg="{t['ip_tip']}">{t['ip']}</span>
                        </div>
                        <div class="mono">{ctx['ip_local']}</div>
                    </div>
                    <div class="metric-row"><div>OS Build</div><div class="mono" style="color:var(--muted)">{ctx['os_version']}</div></div>
                </div>

                <!-- Resources -->
                <div class="card">
                    <div class="card-head">{t['load']} <div class="tip help-icon" data-msg="{t['load_tip']}">?</div></div>
                    
                    <div class="metric-row">
                        <div class="metric-label">
                            <span class="interactive-text" data-msg="{t['cpu_tip']}">CPU</span> 
                            <span style="color:{c_cpu}">{ctx['cpu_load']}%</span>
                        </div>
                        <div class="bar-bg"><div class="bar-fill" style="width:{ctx['cpu_load']}%; background:{c_cpu}"></div></div>
                    </div>

                    <div class="metric-row">
                        <div class="metric-label">
                            <span class="interactive-text" data-msg="{t['ram_tip']}">RAM</span> 
                            <span style="color:{c_ram}">{ctx['ram_usage']}%</span>
                        </div>
                        <div class="bar-bg"><div class="bar-fill" style="width:{ctx['ram_usage']}%; background:{c_ram}"></div></div>
                    </div>

                    <div class="metric-row">
                        <div class="metric-label">
                            <span class="interactive-text" data-msg="{t['disk_tip']}">DISK</span> 
                            <span style="color:{c_dsk}">{ctx['disk_usage']}%</span>
                        </div>
                        <div class="bar-bg"><div class="bar-fill" style="width:{ctx['disk_usage']}%; background:{c_dsk}"></div></div>
                    </div>
                </div>

                <!-- Attack Surface -->
                <div class="card">
                    <div class="card-head">{t['atk']} <div class="tip help-icon" data-msg="{t['atk_tip']}">?</div></div>
                    {ports_html}
                </div>
            </div>
            <footer>{t['footer']}</footer>
        </div>
    </body>
    </html>
    """

    out_dir = "output"
    if not os.path.exists(out_dir): os.makedirs(out_dir)
    path = os.path.join(out_dir, f"sentinel_report_{lang.lower()}.html")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.abspath(path)