import pickle
from flask import Flask, jsonify, request

from util.preprocess import process_text

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/about')
def about():
    name = request.args.get('name', 'Guest')
    return f"This is the Flask API about page. Hello, {name}!"

# Load the saved models and vectorizer
with open('models/classifier.pkl', 'rb') as file:
    model = pickle.load(file)

with open('models/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('models/label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict_category():
    # Get article text from request
    data = request.get_json()
    article = data['article']
    processed_article = process_text(article)
    vectorized_article = vectorizer.transform([processed_article])
    predicted_category_encoded = model.predict(vectorized_article)
  
    return jsonify({
        'category': predicted_category_encoded[0]
    })

if __name__ == '__main__':
    app.run(debug=True)