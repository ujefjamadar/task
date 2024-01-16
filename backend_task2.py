from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

configurations = {
    1: {"remark": "Hello world"},
    2: {"remark": "my name is ujef"},
}

@app.route('/api/configurations/<int:config_id>', methods=['POST'])  # Change to POST
def update_configuration(config_id):
    if config_id not in configurations:
        return jsonify({"message": "Configuration not found"}), 404

    data = request.get_json()

    if 'remark' not in data:
        return jsonify({"message": "Remark not provided"}), 400

    configurations[config_id]['remark'] = data['remark']

    return jsonify({"message": "success"})

@app.route('/')
def index():
    return render_template('frontend_task2.html')

if __name__ == '__main__':
    app.run(debug=True)
