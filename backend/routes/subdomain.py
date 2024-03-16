from flask import Flask, request, jsonify
import tldextract
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify


subdomain_route = Blueprint('subdomain_route', __name__)

def extract_subdomains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        
        soup = BeautifulSoup(response.text, 'html.parser')

        domain_info = tldextract.extract(url)

        subdomains = set()
        for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe']):
            src = tag.get('src') or ''
            href = tag.get('href') or ''
            if src or href:
                parsed_url = tldextract.extract(src or href)
                subdomains.add(parsed_url.subdomain)
        print(subdomains)        
        return list(subdomains)
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

@subdomain_route.route('/api/getsubdomains', methods=['POST'])
def get_subdomains():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL not provided in the request.'}), 400

    subdomains = extract_subdomains(url)
    return jsonify({'subdomains': subdomains})