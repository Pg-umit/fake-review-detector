from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load your model
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        review_vector = vectorizer.transform([review])
        prediction = model.predict(review_vector)[0]
        result = "Fake" if prediction == 1 else "Genuine"
        return render_template("index.html", prediction=result, review_text=review)

# Run app on Render's required host/port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)


