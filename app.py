from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "✅ Web App is Live! Use /predict to POST data."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])
    return jsonify({"prediction": prediction[0]})