from flask import Flask
from models import Whisky, db, Taste
from flask import render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
db.init_app(app)
app.app_context().push()

@app.route('/')
def hello_world():
    whiskies = Whisky.query.all()
    return render_template('index.html', whisky=whiskies)

@app.route('/<int:id>', methods=['POST', 'GET'])
def whisky(id):
    whisky = Whisky.query.get_or_404(id)
    tastes = []
    for taste in whisky.tastes:
        tastes.append(taste.name)

    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('update.html', whisky=whisky, taste=(', '.join(tastes)))

@app.route('/sortowanie', methods=['POST', 'GET'])
def sortowanie():
    tastes = []
    for name in Taste.query.all():
        tastes.append(name.name)

    if request.method == 'POST':
        tastes_checkbox = []
        for i in tastes:
            a = request.form.get(f"{i}")
            if a != None:
                tastes_checkbox.append(a)
        id = []
        w_name = []
        for i in Whisky.query.all():
            id.append(i.id)
            whisky = Whisky.query.get_or_404(i.id)
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
    whisky = Whisky.query.all()
    whisky_name = []
    for name in whisky:
        whisky_name.append(name.name)

    if request.method == 'POST':
        whisky_chosen = ""
        for i in whisky_name:
            a = request.form.get(f"{i}")
            if a != None:
                whisky_chosen = a
        id = 0
        for x in whisky:
            if x.name == whisky_chosen:
                id = (x.id)
        return redirect(f'/{id}')
    else:
        return render_template('lista_whisky.html')

if __name__ == "__main__":
    app.run(debug=True)
