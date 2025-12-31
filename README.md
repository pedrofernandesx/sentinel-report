# 🛡️ Sentinel Report

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

> **Automated System Audit & Network Recon Tool**  
> *Ferramenta de Auditoria de Sistema e Reconhecimento de Rede*
> *🇧🇷 first, 🇺🇸 bellow*

## 📸 Preview / Visualização

<img width="1138" height="470" alt="Sentinel Report Dashboard v2.2" src="https://github.com/user-attachments/assets/51d5e9a9-af78-463f-b865-eba9fcb0739b" />
*(Screenshot of the generated HTML report / Captura de tela do relatório gerado)*

## 💡 UX & Educational Mode / Modo Educativo

<img width="1265" height="444" alt="Interactive Tooltips" src="https://github.com/user-attachments/assets/7e81af27-aefb-4ebb-9c83-2222ce0723e7" />
*(Interactive tooltips in action / Tooltips interativos em ação)*

---

## 🇧🇷 Português

### ⚡ Sobre o Projeto
**Sentinel Report** é uma ferramenta de automação em Python desenvolvida para administradores de sistemas e estudantes de cibersegurança. Ela realiza uma varredura rápida na máquina host, coletando telemetria vital (CPU, RAM, Disco) e executando um scan de portas na rede local.

O resultado é exportado para um **Dashboard HTML Moderno (Dark Mode)**, apresentando layout em Grid, barras de progresso dinâmicas e foco em UX.

O painel foi projetado não apenas para exibir dados, mas para **educar**:
*   **Tooltips Interativos:** Passe o mouse sobre termos técnicos (como *CPU*, *RAM*, *IP Local*) para ver explicações instantâneas e didáticas.
*   **Aprendizado Contextual:** Ajuda estudantes e usuários a entenderem o que "Portas Abertas" ou "Carga Alta" significam para a segurança do sistema.

### 🛠️ Funcionalidades Principais (v2.2)
*   **Telemetria de Sistema:** Monitoramento em tempo real de CPU, Memória e Disco via `psutil`.
*   **Reconhecimento de Rede:** Port Scanner integrado usando `socket` para detectar portas abertas.
*   **Arquitetura Modular:** Código refatorado em camadas (Scanner, Configuração e Gerador).
*   **Relatórios Inteligentes:** Gera um arquivo HTML único sem dependências externas (CSS injetado).
*   **Feedback Visual:** Cores dinâmicas (Verde/Amarelo/Vermelho) baseadas na carga do sistema.

### 🚀 Como Executar
1.  Clone o repositório:
    ```bash
    git clone https://github.com/pedrofernandesx/sentinel-report.git
    cd sentinel-report
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Inicie a sentinela:
    ```bash
    python main.py
    ```
4.  Verifique a pasta `output/` para ver o relatório!

---

## 🇺🇸 English

### ⚡ About the Project
**Sentinel Report** is a Python automation tool designed for sysadmins and cybersecurity enthusiasts. It performs a quick scan of the host machine, collecting vital telemetry (CPU, RAM, Disk usage) and performing a local network port scan.

The result is exported to a **Modern HTML Dashboard**, featuring CSS Grid layout, dynamic progress bars, and educational tooltips.

The dashboard was designed not just to display data, but to **educate**:
*   **Interactive Tooltips:** Hover over technical terms (like *CPU*, *RAM*, *Local IP*) to see instant, beginner-friendly explanations.
*   **Contextual Learning:** Helps users understand what "Open Ports" or "High Load" actually mean for system security.

### 🛠️ Key Features (v2.2)
*   **System Telemetry:** Real-time monitoring of CPU, Memory, and Disk usage via `psutil`.
*   **Network Recon:** Integrated Port Scanner using `socket` to detect open ports (21, 22, 80, 443, etc.).
*   **Modular Architecture:** Refactored code separating logic, configuration, and presentation.
*   **Smart Reporting:** Generates a standalone HTML file with no external dependencies (CSS injected).
*   **Visual Feedback:** Dynamic color coding (Green/Yellow/Red) based on resource load.

### 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone https://github.com/pedrofernandesx/sentinel-report.git
    cd sentinel-report
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the sentinel:
    ```bash
    python main.py
    ```
4.  Check the `output/` folder for the report!

---

## 📂 Project Structure / Estrutura

```text
sentinel-report/
│
├── src/                 # Source Code (Código Fonte)
│   ├── config.py        # Settings, CSS styles & Translations
│   ├── scanner.py       # System & Network collection logic
│   └── generator.py     # HTML injection engine
│
├── output/              # Generated reports (Relatórios gerados)
├── assets/              # Images and static files
├── main.py              # Entry point (Arquivo principal)
└── requirements.txt     # Dependencies