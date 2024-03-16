from flask import Blueprint, request, jsonify
from urllib.parse import urlparse
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import tldextract
import socket

getIP_route = Blueprint('getIP_route', __name__)
@getIP_route.route('/api/getIP_route', methods=['POST'])
def hostname_to_ip():

    hostname = request.json.get('hostname')

    if not hostname:
        return jsonify({'error': 'Hostname parameter is required'}), 400

    try:
    
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        return jsonify({'error': 'Failed to resolve hostname'}), 500

    return jsonify({'ip_address': ip_address})

if __name__ == '__main__':
    app.run(debug=True)
