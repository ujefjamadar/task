from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
configuration_data = {
    'data': [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['8', '9', '0']
    ],
    
}

@app.route('/')
def index():
    return render_template('frontend_task1.html')

@app.route('/api/configurations/<string:config_id>', methods=['GET'])
def get_configuration(config_id):
    if config_id in configuration_data:
        result = configuration_data[config_id]
        return jsonify(result)
    else:
        return jsonify({'error': 'Configuration not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)




#http://localhost:8080/api/configurations/data :for postman