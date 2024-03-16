from flask import Blueprint, request, jsonify
from urllib.parse import urlparse
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import tldextract
import socket


analyzeurl_route = Blueprint('analyzeurl_route', __name__)

API_URL = f'http://localhost:5000/api/domain'

@analyzeurl_route.route('/api/analyze', methods=['POST'])
def analyze_website():
  
    url = request.json.get('url')
    
    
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch website content'}), 500

   
    soup = BeautifulSoup(response.text, 'html.parser')

    domain_info = tldextract.extract(url)

   
    subdomains = set()
    for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe']):
        src = tag.get('src') or ''
        href = tag.get('href') or ''
        if src or href:
            parsed_url = tldextract.extract(src or href)
            subdomains.add(parsed_url.subdomain)


    external_domains = set()
    for tag in soup.find_all(['link', 'script', 'img', 'iframe', 'a']):
        src = tag.get('src') or ''
        href = tag.get('href') or ''
        if src or href:
            parsed_url = tldextract.extract(src or href)
            if parsed_url.subdomain and parsed_url.subdomain not in subdomains:
                external_domains.add(parsed_url.domain + '.' + parsed_url.suffix)

    
    hostname = response.headers.get('Server')
    # print(hostname + ".com")
   
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
           
            print(data)
            # return jsonify(data)
        else:
            return jsonify({'error': 'Failed to trigger another API'}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to trigger another API: {str(e)}'}), 500
    
    
    response_data = {
        'domain_info': {
            'ip_address': ip_address,
            'server_host': response.headers.get('Server'),
            'hostname': hostname+".com",  
            'data':data
        },
       
        'subdomains': list(subdomains),
        'external_domains': list(external_domains)
    }

    return jsonify(response_data)