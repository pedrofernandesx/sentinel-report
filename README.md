# 🛡️ Sentinel Report v2.2

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-v2.2-success?style=flat)

<img width="294" height="101" alt="image" src="https://github.com/user-attachments/assets/611e8eda-55ef-4c02-9ccc-474645c2f1f7" />

* **Automated System Audit & Network Recon Tool**
* *Ferramenta de Auditoria de Sistema e Reconhecimento de Rede*

---

## Dashboard Preview

<img width="100%" alt="Sentinel Report Dashboard v2.2" src="https://github.com/user-attachments/assets/a4ab6198-930f-4e9d-a0ee-2eb50c9a5a2e" />

---

## 🚀 What's New in v2.2 / Novidades da versão 2.2

This version focuses on **Usability** and **User Experience**.
*   *Esta versão foca em **Usabilidade** e **Experiência do Usuário**.*

### 🌍 Multi-language Support (PT/EN)
Now you can choose your preferred language at startup.
*   **Agora você pode escolher entre Português ou Inglês ao iniciar o script.**

### 💻 Cross-platform Support
*   **Linux & Windows:** Validated on Windows 11 and Linux.
*   **Multiplataforma:** Validado em Windows 11 e Linux.

### 🎨 Modern UI & Educational UX
Redesign completo do HTML report.
*   **Visual SaaS:** Clean "Dark Mode" interface for better data visualization.
*   *"Modo Escuro" para melhor visualização de dados.**
*   **Interactive Tooltips:** Hover over metrics (CPU, RAM, Ports) to learn *why* they matter for security.
*   *"Dicas de ferramentas interativas"*
*   **Feedback Visual:** Dynamic colors (Green/Yellow/Red) based on system load.
*   *"Cores dinâmicas com base na carga do sistema."

<img width="494" height="300" alt="image" src="https://github.com/user-attachments/assets/96f5317b-9af8-4515-990d-3ee803178ac1" />


---

## 🛠️ Tech Stack / Tecnologias
*   **Core:** Python (`psutil`, `socket`).
*   **Architecture:** MVC (Modular structure / Estrutura modular).
*   **Frontend:** HTML5/CSS3 (Generated natively / Gerado nativamente)

---

## ⚡ Quick Start / Como Rodar

```bash
# 1. Clone the repository
git clone 
cd sentinel-report

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Sentinel
python main.py

```
O resultado é exportado para um Dashboard em HTML apresentando layout em Grid, barras de progresso dinâmicas e tooltips explicativos.


## 📂 Project Structure / Estrutura

```text
sentinel-report/
│
├── src/                 # Source Code (Código Fonte)
│   ├── config.py        # Settings & Translations
│   ├── scanner.py       # System & Network collection logic
│   └── generator.py     # HTML/CSS injection engine
│
├── output/              # Generated reports (Relatórios gerados)
├── assets/              # Images and static files
├── main.py              # Entry point (Arquivo principal)
└── requirements.txt     # Dependencies
```
👨‍💻 Author
Developed by Pedro Fernandes
