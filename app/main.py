from flask import Flask, request, jsonify
# from flask_limiter.util import get_remote_address
# from flask_limiter import Limiter
import scraper
import utils

app = Flask(__name__)

# Set up rate limiting
# limiter = Limiter(
#     app,
#     key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"]
# )

@app.route('/scrape', methods=['POST'])
# @limiter.limit("10 per minute")
def scrape_site():
    url = request.json.get('url')
    selector = request.json.get('selector', None)
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        data = scraper.scrape(url, selector)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.errorhandler(429)
# def ratelimit_error(e):
#     return utils.rate_limit_response(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)