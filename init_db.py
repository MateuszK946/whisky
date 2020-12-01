from flask import Flask
from models import Whisky, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
app.app_context().push()

sample_data = [
    Whisky(name="Dalmore Cigar Malt Reserve", country="Scotland", taste="Sweet", image="static/img/dalmore-cigar-malt-reserve.jpg"),
    Whisky(name="Glenmorangie Signet", country="Scotland", taste="Sweet", image="static/img/glenmorangie-signet.jpg"),
    Whisky(name="Johnnie Walker Blue Label", country="Scotland", taste="Sweet", image="static/img/johnnie-walker-blue-label.jpg")
]

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    db.session.commit()

    for data in sample_data:
        db.session.add(data)
    db.session.commit()