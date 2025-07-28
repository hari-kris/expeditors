# Step 1: Import and configure APM before creating the Flask app
from elasticapm.contrib.flask import ElasticAPM
import elasticapm
from flask import Flask

# Step 2: Optional - Manually initialize the agent (used if you want more control)
elasticapm.instrument()

# Step 3: Create Flask app
app = Flask(__name__)

# Step 4: Elastic APM configuration
app.config['ELASTIC_APM'] = {
    # Set the service name you want to see in APM UI
    'SERVICE_NAME': 'flask-sample-app',

    # Set the APM Server URL
    'SERVER_URL': 'http://localhost:8200',

    # Optional: Secret token or API key if required by the APM Server
    # 'SECRET_TOKEN': 'your_secret_token',

    # Enable logging errors
    'CAPTURE_ERRORS': True
}

# Step 5: Initialize APM with Flask app
apm = ElasticAPM(app)

# Sample route
@app.route('/')
def hello_world():
    return 'Hello World'

# Main driver
if __name__ == '__main__':
    app.run(debug=True)
