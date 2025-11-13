README.bd:

# SOCF-SO-CLOUD

Projeto de Sistemas Operacionais em Cloud - Análise de PaaS

## 📋 Descrição

Este projeto implementa um servidor web em Flask que expõe informações do sistema operacional através de APIs REST. O objetivo é compreender como serviços de PaaS (Platform as a Service) abstraem o gerenciamento de sistemas operacionais.

## 👥 Equipe

- Gabriel Zem Muraro
- Joao Pedro Bezerra

## 🚀 Funcionalidades

O servidor web oferece três rotas principais:

### / - Página Principal
Exibe todas as informações do sistema em formato HTML:
- Nome dos integrantes da equipe
- PID (Process ID) do processo
- Memória utilizada (em MB)
- Uso de CPU (%)
- Sistema Operacional detectado

### /info - Informações da Equipe
Retorna um JSON com os nomes dos integrantes:
json
{
  "integrantes": "Gabriel Zem Muraro e Joao Pedro Bezerra"
}


### /metricas - Métricas do Sistema
Retorna um JSON com as métricas do sistema:
json
{
  "pid": 1234,
  "memoria_mb": 25.6,
  "cpu_percent": 3.4,
  "sistema_operacional": "Linux (Ubuntu)"
}


## 🛠 Tecnologias Utilizadas

- *Python 3* - Linguagem de programação
- *Flask* - Framework web
- *Gunicorn* - Servidor WSGI para produção
- *psutil* - Biblioteca para informações do sistema
- *Render.com* - Plataforma PaaS para hospedagem

## 📦 Instalação e Execução Local

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
bash
git clone https://github.com/Gabriel-Zem-Muraro/SOCF-SO-CLOUD.git
cd SOCF-SO-CLOUD


2. Crie um ambiente virtual (recomendado):
bash
python -m venv venv


3. Ative o ambiente virtual:
- Windows:
bash
venv\Scripts\activate

- Linux/Mac:
bash
source venv/bin/activate


4. Instale as dependências:
bash
pip install -r requirements.txt


5. Execute o servidor:
bash
python app.py


6. Acesse no navegador:

http://localhost:5000


## 🌐 Aplicação Hospedada

A aplicação está disponível online em: [URL será adicionada após o deploy]

## 📊 Deploy no Render.com

### Configurações Utilizadas
- *Runtime*: Python 3
- *Build Command*: pip install -r requirements.txt
- *Start Command*: gunicorn app:app
- *Instance Type*: Free
- *Branch*: main

### Passos para Deploy
1. Criar conta no Render.com usando GitHub
2. Conectar o repositório SOCF-SO-CLOUD
3. Configurar o Web Service com os parâmetros acima
4. Aguardar o deploy automático

## 📝 Estrutura do Projeto


SOCF-SO-CLOUD/
│
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── README.md             # Documentação do projeto
└── .gitignore            # Arquivos ignorados pelo Git


## 🔍 Análise: PaaS e Abstração do Sistema Operacional

O uso de PaaS como o Render.com demonstra um equilíbrio interessante entre visibilidade e abstração do sistema operacional:

*Aspectos Visíveis:*
- Informações de processo (PID, uso de memória e CPU)
- Identificação do sistema operacional base
- Gerenciamento básico de processos da aplicação

*Aspectos Abstraídos:*
- Configuração e gerenciamento do kernel
- Alocação de hardware físico
- Configuração de rede e firewall
- Provisionamento de armazenamento
- Escalabilidade automática e balanceamento de carga
- Atualizações e patches de segurança do SO

Esta abstração permite que desenvolvedores foquem na lógica da aplicação, enquanto a plataforma cuida da infraestrutura subjacente.
