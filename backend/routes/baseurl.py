from flask import Blueprint, request, jsonify
from urllib.parse import urlparse


baseurl_route = Blueprint('baseurl_route', __name__)

@baseurl_route.route('/api/baseurl', methods=['POST'])
def get_base_url():
   
    url = request.json.get('url')

   
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

   
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    return jsonify({'base_url': base_url})
