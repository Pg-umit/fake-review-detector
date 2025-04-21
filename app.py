from flask import Flask, render_template, request

app = Flask(__name__)

# Define smarter keyword-based logic
positive_keywords = ['genuine', 'authentic', 'original', 'legit', 'satisfied', 'real', 'honest', 'trusted']
negative_keywords = ['scam', 'fake', 'fraud', 'dishonest', 'lie', 'unreal', 'duplicate', 'copy']

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    review = ''
    
    if request.method == 'POST':
        review = request.form['review'].strip()
        review_lower = review.lower()

        if any(word in review_lower for word in positive_keywords):
            result = "Real ✅"
        elif any(word in review_lower for word in negative_keywords):
            result = "Fake ❌"
        else:
            result = "Uncertain 🤔"

    return render_template('index.html', result=result, review=review)

if __name__ == '__main__':
    app.run(debug=True)






