from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/guess', methods=['POST'])
def guess_number():
    data = request.json
    guess = data['guess']
    
    if 'number' not in app.config:
        app.config['number'] = random.randint(1, 100)
    
    if guess < app.config['number']:
        return jsonify({'result': 'Too low!'})
    elif guess > app.config['number']:
        return jsonify({'result': 'Too high!'})
    else:
        return jsonify({'result': f'Congratulations! You guessed the number {app.config["number"]}.'})

if __name__ == '__main__':
    app.run(debug=True)