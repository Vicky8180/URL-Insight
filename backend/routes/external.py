from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
from urllib.parse import urlparse
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import tldextract

external_route = Blueprint('external_route', __name__)

def extract_external_domains(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

       
        stylesheets = [link['href'] for link in soup.find_all('link', rel='stylesheet') if link.get('href')]
        stylesheet_domains = set(urlparse(stylesheet).netloc for stylesheet in stylesheets)

     
        scripts = [script['src'] for script in soup.find_all('script') if script.get('src')]
        script_domains = set(urlparse(script).netloc for script in scripts)

        images = [img['src'] for img in soup.find_all('img') if img.get('src')]
        image_domains = set(urlparse(image).netloc for image in images)

    
        iframes = [iframe['src'] for iframe in soup.find_all('iframe') if iframe.get('src')]
        iframe_domains = set(urlparse(iframe).netloc for iframe in iframes)

    
        anchors = [a['href'] for a in soup.find_all('a') if a.get('href')]
        anchor_domains = set(urlparse(anchor).netloc for anchor in anchors)

        return {
            'stylesheets': list(stylesheet_domains),
            'scripts': list(script_domains),
            'images': list(image_domains),
            'iframes': list(iframe_domains),
            'anchors': list(anchor_domains)
        }
    else:
        return None

@external_route.route('/api/getexternaldomains', methods=['POST'])
def get_external_domains():
    data = request.json
    url = data.get('url')

    if url:
        result = extract_external_domains(url)
        if result:
            return jsonify({'external_domains': [result]})
        else:
            return jsonify({'error': 'Unable to fetch data from the provided URL.'}), 400
    else:
        return jsonify({'error': 'URL not provided in the request.'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
