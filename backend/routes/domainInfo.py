from flask import Flask, request, jsonify
from flask import Blueprint, request, jsonify
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import tldextract
import requests

domain_route = Blueprint('domain_route', __name__)

API_KEY = '87b24208bba84784ac40468fce20e0f6'
API_URL = f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip='

@domain_route.route('/api/domain', methods=['POST'])
def ip_info():
    
    
    ip_address = request.json.get('ip')
    print(ip_address)

    if not ip_address:
        return jsonify({'error': 'IP parameter is required'}), 400

    try:
      
        response = requests.get(API_URL + ip_address)
        response.raise_for_status()  

    
        data = response.json()
        # print(data)
      
        fetched_info = {
            'ip': data.get('ip'),
            'country': data.get('country_name'),
            'city': data.get('city'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'asn': data.get('asn'),
            'isp': data.get('isp'),
            'organization': data.get('organization')
        }

        return jsonify( fetched_info)

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch information: {str(e)}'}), 500
