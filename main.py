from flask import Flask
from models import Whisky, db
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
db.init_app(app)
app.app_context().push()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<int:id>')
def whisky(id = None):
    return render_template('index.html', id = id)

if __name__ == "__main__":
    app.run(debug=True)
    