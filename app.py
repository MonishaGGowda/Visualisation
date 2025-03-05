from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Define a Prometheus Counter metric
REQUEST_COUNT = Counter("request_count", "Total number of requests")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello, World!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
