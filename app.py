from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    review = ''

    if request.method == 'POST':
        review = request.form.get('review', '').lower()
        suspicious_signs = 0

        # 1. Repeating words
        if re.search(r'\b(\w+)\s+\1\b', review):
            suspicious_signs += 1

        # 2. Emoji overload
        if len(re.findall(r'[😀-🙏🚀✨❤️⭐🌟💯🔥🎉😁😂😅😍]', review)) > 3:
            suspicious_signs += 1

        # 3. Promotional or exaggerated language
        promo_phrases = [
            r"must[\s\-]?buy", r"life[\s\-]?changing", r"highly[\s\-]?recommend", 
            r"100%[\s\-]?satisfied", r"best[\s\-]?ever", r"superb", r"outstanding", r"perfect"
        ]
        for phrase in promo_phrases:
            if re.search(phrase, review):
                suspicious_signs += 1
                break

        # 4. Too short
        if len(review.split()) < 6:
            suspicious_signs += 1

        # 5. Too many exclamation marks
        if review.count("!") > 3:
            suspicious_signs += 1

        # Final rule: 1 or more signs = Fake
        result = "Fake" if suspicious_signs >= 1 else "Real"

    return render_template('index.html', result=result, review=review)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)









