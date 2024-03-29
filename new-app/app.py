from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Adjust the symbols to improve the odds of winning
symbols =  ['D', 'C', 'C', 'S', 'M', 'J', 'L']

def shuffle_reel():
    return [random.choice(symbols) for _ in range(4)]  # Change 3 to 4

def get_payout(playline):
    if 'C' in playline:  # Check if "C" is present in the playline
        return 0  # No payout if "C" is present
    elif playline.count('D') == 4:  # Change 3 to 4
        return 500
    elif playline.count('S') == 4:  # Change 3 to 4
        return 10000
    elif playline.count('M') == 4:  # Change 3 to 4
        return 10000
    elif playline.count('J') == 4:  # Change 3 to 4
        return 10000
    elif playline.count('L') == 4:  # Change 3 to 4
        return 10000
    elif playline.count('S') == 3:  # Payout for 3 'S'
        return 500
    elif playline.count('M') == 3:  # Payout for 3 'M'
        return 500
    elif playline.count('J') == 3:  # Payout for 3 'J'
        return 500
    elif playline.count('L') == 3:  # Payout for 3 'L'
        return 500
    elif playline.count('S') == 2:  # Payout for 2 'S'
        return 100
    elif playline.count('M') == 2:  # Payout for 2 'M'
        return 100
    elif playline.count('J') == 2:  # Payout for 2 'J'
        return 100
    elif playline.count('L') == 2:  # Payout for 2 'L'
        return 100
    elif set(playline) == {'S', 'M', 'J', 'L'}:  # Check if all four symbols are present
        return 50000  # Jackpot for S-M-J-L combination
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
