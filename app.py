from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('knn_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

@app.route('/')
def home():
    return render_template('index.html', result=None, review_text='')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    review_vec = vectorizer.transform([review])
    prediction = model.predict(review_vec)[0]
    result = "Genuine ✅" if prediction >= 0.5 else "Fake ❌"
    return render_template('index.html', result=result, review_text=review)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

