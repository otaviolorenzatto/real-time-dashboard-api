# 🖥️ Dashboard de Monitoramento de Sistema

Este projeto consiste em um **dashboard de monitoramento em tempo real** do uso de **CPU**, **memória RAM** e **disco** de um computador. Os dados são coletados continuamente, enviados para um servidor Redis, e disponibilizados aos usuários através de uma interface web via WebSocket.

---

## 🚀 Tecnologias Utilizadas

- **Python** + **psutil**: Coleta dos dados de sistema (CPU, RAM, Disco).
- **Redis**: Armazenamento temporário (cache) dos dados coletados.
- **Tornado (Python)**: WebSocket server para envio dos dados em tempo real aos clientes.
- **HTML + CSS + JS**: Interface frontend para exibição do dashboard.
- **dotenv**: Gerenciamento de variáveis de ambiente.

---

## 📦 Requisitos

Instale as dependências listadas no `requirements.txt`:

```
dotenv==0.9.9
psutil==7.0.0
python-dotenv==1.1.1
redis==6.2.0
tornado==6.5.1
```

---

## 🛠️ Como Executar o Projeto

1. Clone este repositório:

```bash
git clone https://github.com/jeanvanz/real-time-dashboard-api.git
cd real-time-dashboard-api
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv env
source env/bin/activate  # Linux
env\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
REDIS_HOST=""
REDIS_PORT=""
REDIS_PASSWORD=""
```

5. Execute os módulos de coleta de dados `redis_pub.py` e o servidor WebSocket `main.py`.

