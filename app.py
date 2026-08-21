from flask import Flask, jsonify
from database import init_db

app = Flask(__name__)

# Inicializar la base de datos al levantar el script
init_db()

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "online",
        "message": "Servidor del Torneo de Robótica activo"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)