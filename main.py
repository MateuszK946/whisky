from flask import Flask
from models import Whisky, db, Taste
from flask import render_template, request, redirect, session
from random import randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
db.init_app(app)
app.app_context().push()

@app.route('/')
def hello_world():
    whiskies = Whisky.query.all()
    rand1 = randint(0, 377)
    rand2 = randint(0, 377)
    rand3 = randint(0, 377)
    if rand2 == rand1 and rand2:
        rand2 = randint(0, 377)
    if rand3 == rand1 or rand3 == rand2:
        rand3 = randint(0, 377)
    return render_template('index.html', whisky=whiskies, rand1=rand1, rand2=rand2, rand3=rand3)

@app.route('/<int:id>', methods=['POST', 'GET'])
def whisky(id):
    whisky = Whisky.query.get_or_404(id)
    tastes = [taste.name for taste in whisky.tastes]

    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('update.html', whisky=whisky, taste=(', '.join(tastes)))

@app.route('/sortowanie', methods=['POST', 'GET'])
def sortowanie():
    tastes = [taste.name for taste in Taste.query.all()]

    if request.method == 'POST':
        tastes_checkbox = []
        for taste in tastes:
            chosen_taste = request.form.get(f"{taste}")
            if chosen_taste != None:
                tastes_checkbox.append(chosen_taste)
        id = []
        w_name = []
        for whisky_id in Whisky.query.all():
            id.append(whisky_id.id)
            whisky = Whisky.query.get_or_404(whisky_id.id)
            tastes_in_whisky = []
            for taste in whisky.tastes:
                tastes_in_whisky.append(taste.name)
                if tastes_checkbox != [] and all(elem in tastes_in_whisky for elem in tastes_checkbox):
                    w_name.append(whisky.name)
                    tastes_in_whisky.clear()
        return render_template('lista_whisky.html', w_name=w_name, whisky_id=whisky)
    else:
        return render_template('sortowanie.html', taste=tastes) # taste=(', '.join(tastes)))

@app.route('/list', methods=['POST', 'GET'])
def list():
    whiskies = Whisky.query.all()
    whisky_name = [whisky.name for whisky in whiskies]

    if request.method == 'POST':
        whisky_chosen = ""
        for name in whisky_name:
            choice = request.form.get(f"{name}")
            if choice != None:
                whisky_chosen = choice
        id = 0
        for whisky_id in whiskies:
            if whisky_id.name == whisky_chosen:
                id = (whisky_id.id)
        return redirect(f'/{id}')
    else:
        return render_template('lista_whisky.html')

@app.route('/random', methods=['POST', 'GET'])
def random():
    ids = [whisky.id for whisky in Whisky.query.with_entities(Whisky.id).distinct()]
    random_id = choice(ids)
    return redirect(f'/{random_id}')

if __name__ == "__main__":
    app.run(debug=True)
