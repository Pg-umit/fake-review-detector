from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    review = ''
    if request.method == 'POST':
        review = request.form.get('review', '')
        result = "Real" if "genuine" in review.lower() else "Fake"
    return render_template('index.html', result=result, review=review)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)





