from flask import Flask, jsonify
import socket
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        database=os.environ.get('DB_NAME', 'myapp'),
        user=os.environ.get('DB_USER', 'appuser'),
        password=os.environ.get('DB_PASSWORD', '')
    )
    return conn

@app.route('/')
def hello():
    hostname = socket.gethostname()
    env = os.getenv('ENV', 'unknown')
    return f"Hello from {hostname} in {env} environment!"

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
