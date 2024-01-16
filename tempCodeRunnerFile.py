from flask import Flask, jsonify, request

app = Flask(__name__)


configurations = [
    {"id": 1, "remark": "Hello world"},
    {"id": 2, "remark": "My name is Ujef"},
    {"id": 3, "remark": "Im fresher"},
    
]

#
@app.route("/api/configurations/<int:configuration_id>", methods=["PUT"])
def update_remark(configuration_id):
   
    if 0 <= configuration_id < len(configurations):
       
        config = configurations[configuration_id]
        new_remark = request.json.get("remark")

        config["remark"] = new_remark

        return jsonify({"message": "success"})
    else:
        return jsonify({"error": "Invalid configurationId"}), 404

if __name__ == "__main__":
    app.run(debug=True)
