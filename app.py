from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model and vectorizer
model = joblib.load('knn_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']  # Get review text from form

        # Transform review using the vectorizer
        review_vec = vectorizer.transform([review])

        # Make prediction
        prediction = model.predict(review_vec)[0]

        # Determine result
        result = "Genuine ✅" if prediction >= 0.5 else "Fake ❌"

        # Pass result and review back to template so textarea retains it
        return render_template('index.html', result=result, review_text=review)

if __name__ == '__main__':
    app.run(debug=True)

