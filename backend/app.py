from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_model import predict_traffic

app = Flask(__name__)
CORS(app)


@app.route('/process_input', methods=['POST'])
def process_input():
    input_data = request.json

    day_value = input_data.get('day')
    hour_value = input_data.get('hour')
    
    day_value = int(day_value)
    hour_value = int(hour_value)

    prediction_map_values = predict_traffic(day_value, hour_value)

    result = {
        'predictions': prediction_map_values.to_dict(orient='records')
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
