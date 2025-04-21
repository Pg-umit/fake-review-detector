from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    review = ''
    
    if request.method == 'POST':
        review = request.form.get('review', '').lower()

        # Flags that suggest fake patterns
        suspicious_signs = 0
        
        # 1. Repeating words (common in bot-written reviews)
        if re.search(r'\b(\w+)\s+\1\b', review):
            suspicious_signs += 1
        
        # 2. Excessive use of emojis (can be overhyped)
        if len(re.findall(r'[😀-🙏🚀✨❤️⭐🌟💯🔥]', review)) > 5:
            suspicious_signs += 1

        # 3. Overly promotional language
        promo_words = ['must buy', '100% satisfied', 'life changing', 'highly recommend']
        for phrase in promo_words:
            if phrase in review:
                suspicious_signs += 1

        # 4. Length check — extremely short reviews
        if len(review.split()) < 5:
            suspicious_signs += 1

        # Final decision
        result = "Fake" if suspicious_signs >= 2 else "Real"

    return render_template('index.html', result=result, review=review)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)








