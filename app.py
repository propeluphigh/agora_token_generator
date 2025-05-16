from flask import Flask, request, jsonify
from flask_cors import CORS
from agora_token_builder import RtcTokenBuilder
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Get Agora credentials from environment variables
APP_ID = os.getenv('APP_ID')
APP_CERTIFICATE = os.getenv('APP_CERTIFICATE')

# Define role constants
ROLE_PUBLISHER = 1  # Host/Publisher
ROLE_SUBSCRIBER = 2  # Audience/Subscriber

@app.route('/ping', methods=['GET'])
def ping():
    """Health check endpoint"""
    return jsonify({"message": "pong"})

@app.route('/getToken', methods=['POST'])
def get_token():
    """Generate token based on request parameters"""
    try:
        data = request.get_json()
        
        # Get parameters from request
        channel_name = data.get('channel', '')
        uid = data.get('uid', 0)  # If not provided, use 0 for random uid
        role = data.get('role', 'publisher')
        token_type = data.get('tokenType', 'rtc')
        expire_time = data.get('expire', 3600)  # Default 1 hour
        
        # Calculate privilege expire time
        privilege_expired_ts = int(time.time()) + expire_time
        
        # Generate token based on token type
        if token_type == 'rtc':
            # Determine role
            role_value = ROLE_PUBLISHER if role == 'publisher' else ROLE_SUBSCRIBER
            
            # Generate RTC token
            token = RtcTokenBuilder.buildTokenWithUid(
                APP_ID,
                APP_CERTIFICATE,
                channel_name,
                uid,
                role_value,
                privilege_expired_ts
            )
            
            return jsonify({
                "token": token,
                "uid": uid
            })
            
        else:
            return jsonify({
                "error": "Unsupported token type"
            }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port) 
