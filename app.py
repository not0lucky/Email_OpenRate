from flask import Flask, send_file, request
from flask_cors import CORS
import logging
from io import BytesIO

app = Flask(__name__)
CORS(app)  # This will allow all domains to access the server

logging.basicConfig(level=logging.INFO)

@app.route('/track', methods=['GET'])
def track_email():
    # Log the request (email parameter)
    email = request.args.get('email')
    logging.info(f"Email tracked: {email}")

    # Serve the 1x1 transparent pixel
    pixel = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\xf3\xff\xff\x00\x00\x00\x00IEND\xaeB`\x82'
    pixel_image = BytesIO(pixel)
    return send_file(pixel_image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
