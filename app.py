from flask import Flask, render_template, request
import random

app = Flask(__name__)

secret_number = random.randint(1, 5)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        guess = request.form.get('guess')
        if guess:
            if int(guess) == secret_number:
                message = "🎉 Correct! You guessed the number!"
            else:
                message = "❌ Nope! Try again."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)


