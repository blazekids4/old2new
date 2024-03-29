from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Adjust the symbols to improve the odds of winning
symbols =  ['D', 'D', 'C', 'C', 'C', 'S', 'M', 'J', 'L']

def shuffle_reel():
    return [random.choice(symbols) for _ in range(3)]

def get_payout(playline):
    if 'C' in playline:  # Check if "C" is present in the playline
        return 0  # No payout if "C" is present
    elif playline.count('D') == 2:
        return 500
    elif playline.count('S') == 3:
        return 10000
    elif playline.count('M') == 3:
        return 10000
    elif playline.count('J') == 3:
        return 10000
    elif playline.count('L') == 3:
        return 10000
    elif playline.count('S') in [1, 2]:
        return 50
    elif playline.count('M') in [1, 2]:
        return 50
    elif playline.count('J') in [1, 2]:
        return 50
    elif playline.count('L') in [1, 2]:
        return 50
    elif ''.join(sorted(playline)) == 'JML':
        return 50000  # Jackpot for J-M-L combination
    return 0


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route("/")
def slot_machine():
    config_balance = request.args.get("player_balance", default=100, type=int)

    playline = shuffle_reel()
    payout = get_payout(playline)
    config_balance += payout

    return jsonify({'playline': playline, 'payout': payout, 'balance': config_balance})

if __name__ == "__main__":
    app.run(debug=True)
