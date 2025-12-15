# app.py

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from recommender import get_recommendations

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()

        region = data.get('region')
        budget = data.get('budget')
        interest = data.get('interest')

        if not all([region, budget, interest]):
            return jsonify({"error": "Missing parameters"}), 400

        recommendations = get_recommendations(region, budget, interest)
        return jsonify(recommendations)

    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000/")
    app.run(debug=True)
