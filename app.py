from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

TEAM_MEMBERS = "Gabriel Zem Muraro e Joao Pedro Bezerra"

def get_system_info():
    process = psutil.Process(os.getpid())
    
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)
    
    cpu_percent = process.cpu_percent(interval=0.1)
    
    os_name = platform.system()
    os_version = platform.release()
    os_full = f"{os_name} ({platform.platform()})"
    
    return {
        "nome": TEAM_MEMBERS,
        "pid": os.getpid(),
        "memoria_mb": round(memory_mb, 2),
        "cpu_percent": round(cpu_percent, 2),
        "sistema_operacional": os_full
    }

@app.route('/')
def home():
    info = get_system_info()
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SOCF - Sistemas Operacionais em Cloud</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                border-bottom: 3px solid #4CAF50;
                padding-bottom: 10px;
            }}
            .info-item {{
                margin: 15px 0;
                padding: 10px;
                background-color: #f9f9f9;
                border-left: 4px solid #4CAF50;
            }}
            .label {{
                font-weight: bold;
                color: #555;
            }}
            .value {{
                color: #333;
                margin-left: 10px;
            }}
            .routes {{
                margin-top: 30px;
                padding: 20px;
                background-color: #e3f2fd;
                border-radius: 10px;
                border: 2px solid #2196F3;
            }}
            .routes h2 {{
                color: #1565c0;
                margin-top: 0;
                margin-bottom: 20px;
            }}
            .route-item {{
                background-color: white;
                padding: 15px;
                margin: 15px 0;
                border-radius: 8px;
                border-left: 5px solid #2196F3;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .route-path {{
                font-family: 'Courier New', monospace;
                font-size: 18px;
                font-weight: bold;
                color: #1976d2;
                margin-bottom: 8px;
            }}
            .route-path a {{
                color: #1976d2;
                text-decoration: none;
            }}
            .route-path a:hover {{
                text-decoration: underline;
                color: #0d47a1;
            }}
            .route-description {{
                color: #555;
                line-height: 1.6;
                margin-top: 8px;
            }}
            .route-response {{
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
                font-family: 'Courier New', monospace;
                font-size: 13px;
                color: #333;
            }}
            .emoji {{
                font-size: 20px;
                margin-right: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sistemas Operacionais em Cloud</h1>
            
            <div class="info-item">
                <span class="label">Nome:</span>
                <span class="value">{info['nome']}</span>
            </div>
            
            <div class="info-item">
                <span class="label">PID:</span>
                <span class="value">{info['pid']}</span>
            </div>
            
            <div class="info-item">
                <span class="label">Memória usada:</span>
                <span class="value">{info['memoria_mb']} MB</span>
            </div>
            
            <div class="info-item">
                <span class="label">CPU:</span>
                <span class="value">{info['cpu_percent']}%</span>
            </div>
            
            <div class="info-item">
                <span class="label">Sistema Operacional:</span>
                <span class="value">{info['sistema_operacional']}</span>
            </div>
            
            <div class="routes">
                <h2>Rotas Disponíveis da API</h2>
                
                <div class="route-item">
                    <div class="route-path">
                        <a href="/info" target="_blank">/info</a>
                    </div>
                    <div class="route-description">
                        <strong>O que faz:</strong> Esta rota retorna apenas as informações sobre os 
                        integrantes da equipe. É útil quando você precisa apenas saber quem desenvolveu 
                        o projeto, sem todas as outras informações técnicas.
                    </div>
                    <div class="route-response">
                        <strong>Retorna:</strong> JSON com os nomes dos integrantes<br>
                        Exemplo: {{"integrantes": "Gabriel Zem Muraro e Joao Pedro Bezerra"}}
                    </div>
                </div>
                
                <div class="route-item">
                    <div class="route-path">
                        <a href="/metricas" target="_blank">/metricas</a>
                    </div>
                    <div class="route-description">
                        <strong>O que faz:</strong> Esta rota retorna as métricas técnicas do sistema 
                        em tempo real. Ela coleta informações sobre o processo da aplicação, como 
                        quanto de memória está sendo usada, qual o uso de CPU, e qual sistema operacional 
                        está rodando. Essas informações mudam toda vez que você acessa!
                    </div>
                    <div class="route-response">
                        <strong>Retorna:</strong> JSON com métricas do sistema<br>
                        Exemplo: {{"pid": 1234, "memoria_mb": 25.6, "cpu_percent": 3.4, "sistema_operacional": "Linux"}}
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/info')
def info():
    return jsonify({
        "integrantes": TEAM_MEMBERS
    })

@app.route('/metricas')
def metricas():
    info = get_system_info()
    return jsonify({
        "pid": info["pid"],
        "memoria_mb": info["memoria_mb"],
        "cpu_percent": info["cpu_percent"],
        "sistema_operacional": info["sistema_operacional"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)