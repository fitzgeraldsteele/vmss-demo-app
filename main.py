from flask import Flask, jsonify, render_template
import json
from datetime import datetime

app = Flask(__name__)

def get_instance_metadata():
    # Mock data for demonstration purposes
    mock_metadata = {
        "compute": {
            "azEnvironment": "AzurePublicCloud",
            "name": "mock-vm",
            "location": "eastus",
            "vmSize": "Standard_D2s_v3",
            "osType": "Linux",
        },
        "network": {
            "interface": [
                {
                    "ipv4": {
                        "ipAddress": [
                            {
                                "privateIpAddress": "10.0.0.4",
                                "publicIpAddress": "20.30.40.50"
                            }
                        ]
                    },
                    "macAddress": "000D3A00B00C"
                }
            ]
        }
    }
    return mock_metadata

@app.route('/')
def index():
    metadata = get_instance_metadata()
    formatted_metadata = json.dumps(metadata, indent=2)
    return render_template('index.html', metadata=formatted_metadata)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "VM is functioning normally"
    }), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="404 Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error="500 Internal Server Error"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
