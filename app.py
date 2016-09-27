from flask import Flask, render_template, send_from_directory
import sys
sys.path.insert(0, 'scripts')
from occupation import randomOccupation


app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'homepage.html')

@app.route('/occupations')
def occupations():
    return render_template("occupations.html", **(randomOccupation()))

if __name__ == '__main__':
    app.run()
