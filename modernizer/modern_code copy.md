Modern Code:
### Python Flask Application for ALPHABET SLOTS

You'll need to split the solution into separate files for clarity and organization. 
Let's start with the Flask application file and then move onto the templates and other necessary components.

#### `app.py` - Main Application File

```python
from flask import Flask, request, render_template, redirect, url_for
import random

app = Flask(__name__)

symbols = ['A', 'B', 'C', 'Z', 'D', 'X', 'Y']

def get_symbol(num):
    return symbols[num]

def shuffle_reel():
    return [get_symbol(random.randint(0, 6)) for _ in range(3)]

def check_play_lines(balance, play_lines):
    if play_lines not in [1, 3]:
        return "error, only 1 or 3 lines can be played", True
    if play_lines > balance:
        return "you are broke, restart link", True
    return "", False

def get_payout(playline):
    if playline == ['Z', 'Z', 'Z']:
        return 500
    elif playline == ['Y', 'Y', 'Y']:
        return 100
    # Add more conditions as needed
    return 0

def mark_paytable(paytableamt, ptm):
    return [str(amount) if amount not in ptm else f"<b>{amount}</b>" for amount in paytableamt]

@app.route("/")
def slot_machine():
    config_balance = request.args.get("player_balance", default=100, type=int)
    config_play_lines = request.args.get("player_spins", default=3, type=int)
    config_winnings = 0

    error_message, error_flag = check_play_lines(config_balance, config_play_lines)
    if error_flag:
        return error_message

    reel1 = shuffle_reel()
    reel2 = shuffle_reel()
    reel3 = shuffle_reel()

    config_balance -= config_play_lines

    playlines_and_winnings = []
    for i in range(config_play_lines):
        playline = [reel1[i], reel2[i], reel3[i]]
        payout = get_payout(playline)
        config_winnings += payout
        playlines_and_winnings.append((playline, payout))

    config_balance += config_winnings

    return render_template("slots.html", balance=config_balance, playlines_and_winnings=playlines_and_winnings)

if __name__ == "__main__":
    app.run(debug=True)
```

#### `templates/slots.html` - HTML Template for Displaying Results

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Alphabet Slots</title>
</head>
<body>
    <h1>Welcome to Alphabet Slots!</h1>
    <form action="/" method="get">
        <label for="player_balance">Player Balance:</label>
        <input type="number" id="player_balance" name="player_balance" value="{{ balance }}">
        <label for="player_spins">Play Lines (1 or 3):</label>
        <input type="number" id="player_spins" name="player_spins" min="1" max="3">
        <button type="submit">Spin</button>
    </form>
    <hr>
    <h2>Spin Results</h2>
    {% for playline, payout in playlines_and_winnings %}
    <div>
        <p>Playline: {{ playline }}</p>
        <p>Payout: {{ payout }}</p>
    </div>
    {% endfor %}
</body>
</html>
```

This solution represents the functionality described in the pseudocode. 
Additions such as input validation, more payout conditions, and enhancing the HTML template can further improve the application based on specific requirements.