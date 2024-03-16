from flask import Flask
from flask import request, jsonify
import requests
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import socket
from backend.routes.baseurl import baseurl_route
from backend.routes.analys import analyzeurl_route
from backend.routes.getIP import getIP_route
from backend.routes.domainInfo import domain_route
from backend.routes.external import external_route
from backend.routes.subdomain import subdomain_route



app = Flask(__name__)
# socketio = SocketIO(app)
# CORS(app, origins='http://localhost:3000') 

# app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Socket connected')

@socketio.on('info_domain')
def handle_button_click(button_name):

    data = {
        "url": button_name
    }
    
    response = requests.get(button_name)
    hostname = response.headers.get('Server')
   
    if not hostname:
        return jsonify({'error': 'Hostname parameter is required'}), 400

    try:
       
        ip_address = socket.gethostbyname(hostname+".com")
    except socket.gaierror:
        return jsonify({'error': 'Failed to resolve hostname'}), 500

   
    
    try:
        
        url = 'http://localhost:5000/api/domain'
        payload = {"ip": ip_address}
        response = requests.post(url, json=payload)

   
        if response.status_code == 200:
            data = response.json()
        else:
            return jsonify({'error': 'Failed to trigger another API'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to trigger another API: {str(e)}'}), 500
    
    
    
    
    
    api_response = response.json() if response.status_code == 200 else None
    socketio.emit('messageFromServer', api_response)


@socketio.on('getsubdomain')
def handle_button_click(button_name):
    print(f'Button "{button_name}" clicked')
    data = {
        "url": button_name
    }
    response = requests.post('http://localhost:5000/api/getsubdomains', json=data)
    api_response = response.json() if response.status_code == 200 else None
    socketio.emit('messageFromServer', api_response)

@socketio.on('getexternaldomains')
def handle_button_click(button_name):
   
    data = {
        "url": button_name
    }
    response = requests.post('http://localhost:5000/api/getexternaldomains', json=data)
    api_response = response.json() if response.status_code == 200 else None
    
   
    socketio.emit('messageFromServer',api_response)


app.register_blueprint(baseurl_route)
app.register_blueprint(analyzeurl_route)
app.register_blueprint(getIP_route)
app.register_blueprint(domain_route)
app.register_blueprint(external_route)
app.register_blueprint(subdomain_route)

# 
if __name__ == '__main__':
    socketio.run(app)


