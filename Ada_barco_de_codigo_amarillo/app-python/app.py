import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        dbname=os.environ.get("POSTGRES_DB"),
        port=5432,
    )

@app.route("/")
def index():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        hora_db = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify(status="ok", servicio="python", hora_db=str(hora_db))
    except Exception as e:
        return jsonify(status="error", detalle=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)