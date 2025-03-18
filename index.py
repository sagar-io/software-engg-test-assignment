
from flask import Flask
import subprocess
import pytz
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sagar Sharma"
    
    username = subprocess.check_output(['whoami']).decode().strip()
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    
    response = f"""Name: {name}
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}"""
    
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
