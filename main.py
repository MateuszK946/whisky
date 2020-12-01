from flask import Flask
from models import Whisky, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
db.init_app(app)
app.app_context().push()

@app.route('/')
def hello_world():
    return 'Hello Adam wow!'

if __name__ == "__main__":
    app.run(debug=True)
    