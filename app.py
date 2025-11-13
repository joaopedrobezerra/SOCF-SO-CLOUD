from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(_name_)

# Team members
TEAM_MEMBERS = "Gabriel Zem Muraro e Joao Pedro Bezerra"

def get_system_info():
    """Get system information for the current process"""
    process = psutil.Process(os.getpid())
    
    # Get memory usage in MB
    memory_info = process.memory_info()
    memory_mb = memory_info.rss / (1024 * 1024)
    
    # Get CPU usage percentage
    cpu_percent = process.cpu_percent(interval=0.1)
    
    # Get OS information
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
    """Homepage displaying system information in HTML format"""
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
                background-color: #e8f5e9;
                border-radius: 5px;
            }}
            .routes h2 {{
                color: #2e7d32;
                margin-top: 0;
            }}
            .routes a {{
                color: #1976d2;
                text-decoration: none;
            }}
            .routes a:hover {{
                text-decoration: underline;
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
        </div>
    </body>
    </html>
    """
    return html

@app.route('/info')
def info():
    """Return team member information in JSON format"""
    return jsonify({
        "integrantes": TEAM_MEMBERS
    })

@app.route('/metricas')
def metricas():
    """Return system metrics in JSON format"""
    info = get_system_info()
    return jsonify({
        "pid": info["pid"],
        "memoria_mb": info["memoria_mb"],
        "cpu_percent": info["cpu_percent"],
        "sistema_operacional": info["sistema_operacional"]
    })

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)