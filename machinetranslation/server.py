from flask import Flask, request, render_template
from machinetranslation import english_to_french, french_to_english

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench')
def translate_english_to_french():
    text_to_translate = request.args.get('text')
    translated_text = english_to_french(text_to_translate)
    return translated_text

@app.route('/frenchToEnglish')
def translate_french_to_english():
    text_to_translate = request.args.get('text')
    translated_text = french_to_english(text_to_translate)
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

