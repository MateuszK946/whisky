from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

whisky_tastes = db.Table('whisky_tastes',
    db.Column('taste_name', db.String(80), db.ForeignKey('taste.name'), primary_key=True),
    db.Column('whisky_id', db.Integer, db.ForeignKey('whisky.id'), primary_key=True)
)

class Taste(db.Model):
    name = db.Column(db.String(80), primary_key=True)

class Whisky(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    region = db.Column(db.String(40), nullable=True)
    description = db.Column(db.String(1024), nullable=True)
    list_img_url = db.Column(db.String(256), nullable=True)
    detail_img_url = db.Column(db.String(256), nullable=True)
    tastes = db.relationship('Taste', secondary=whisky_tastes, lazy='subquery',
        backref=db.backref('whiskies', lazy=True))

