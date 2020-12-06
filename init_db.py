from flask import Flask
from models import *
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
app.app_context().push()

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    db.session.commit()

    ### TASTES
    re = requests.get("https://evening-citadel-85778.herokuapp.com:443/tag/")
    page = 0

    while True:
        page += 1
        print(f"Pobieranie {page} strony smaków")
        for taste in re.json()['results']:
            db.session.add(Taste(name=taste['title']))
        if not re.json()['next']:
            break
        else:
            re = requests.get(re.json()['next'])

    db.session.commit()


    ### WHISKIES

    re = requests.get("https://evening-citadel-85778.herokuapp.com:443/whiskey/")
    page = 0

    while True:
        page += 1
        print(f"Pobieranie {page} strony whisky")
        for whisky in re.json()['results']:
            whisky_db = Whisky(id=whisky['id'], name=whisky['title'], region=whisky['region'], 
                description=whisky['description'], list_img_url=whisky['list_img_url'], detail_img_url=whisky['detail_img_url'])
            for tag in whisky['tags']:
                whisky_db.tastes.append(Taste.query.get(tag['title']))
            db.session.add(whisky_db)

        if not re.json()['next']:
            break
        else:
            re = requests.get(re.json()['next'])

    db.session.commit()
