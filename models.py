from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Whisky(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(40), nullable=False)
    taste = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(120), unique=True)
    
    def __repr__(self):
        return f"Whisky {self.name}, {self.country}, {self.taste}"
