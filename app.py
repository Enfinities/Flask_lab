from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

myboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1

def toggle_player():
    global current_player
    current_player = 2 if current_player == 1 else 1

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the row and column from the button clicked
        row_col = request.form.get('row')
        if row_col:
            row, col = map(int, row_col.split('-'))

            # Process the move
            if myboard[row][col] == 0:
                myboard[row][col] = current_player
                toggle_player()
    return render_template('index.html', board=myboard, current_turn=current_player, enumerate=enumerate)

@app.route('/restart', methods=['POST'])
def restart():
    global myboard, current_player
    myboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

