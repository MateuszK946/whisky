from flask import Flask
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
app.app_context().push()

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    db.session.commit()
