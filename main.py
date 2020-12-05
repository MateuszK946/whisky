from flask import Flask
from models import Whisky, db
from flask import render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whisky.db'
db.init_app(app)
app.app_context().push()

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    whiskies = Whisky.query.limit(3).all()
    return render_template('index.html', whisky=whiskies)

@app.route('/<int:id>', methods=['POST', 'GET'])
def whisky(id):
    whisky = Whisky.query.get_or_404(id)

    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('update.html', whisky=whisky)

if __name__ == "__main__":
    app.run(debug=True)
    print(Whisky.query.get_or_404(1))
