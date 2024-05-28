from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    if length < 6:
        raise ValueError("O tamanho da senha deve ser de pelo menos 6 caracteres.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    all_chars = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    return jsonify(password=password)

if __name__ == "__main__":
    app.run(debug=True)