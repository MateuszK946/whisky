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
        print(taste.name)
        tastes.append(taste.name)
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('update.html', whisky=whisky, taste=(', '.join(tastes)))

@app.route('/sortowanie', methods=['POST', 'GET'])
def sortowanie():
    whisky = Whisky.query.all()
    tastes = []
    for name in Taste.query.all():
        tastes.append(name.name)

    if request.method == 'POST':
        # taste0 = request.form.get('taste0')
        # taste1 = request.form.get('taste1')
        # taste2 = request.form.get('taste2')
        # print(taste0, taste1, taste2)
        # if taste0 or taste1 or taste2 in whisky.tastes:
        #     print(whisky.name)
        return redirect('/')
    else:
        return render_template('sortowanie.html', taste=tastes) # taste=(', '.join(tastes)))

@app.route('/lista', methods=['POST', 'GET'])
def lista():
    pass

if __name__ == "__main__":
    app.run(debug=True)