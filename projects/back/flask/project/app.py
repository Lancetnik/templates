from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import SomeModel, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/', methods=['post', 'get'])
def hello_world():
    return 'Hello, World!!!!'


@app.route('/main/', methods=['get'])
def main_render():
    return render_template('index.html')


@app.route('/post/', methods=['post'])
def some_post():
    data = json.loads(request.data)
    return jsonify(data)


@app.route('/create/', methods=['post'])
def create_data():
    data = json.loads(request.data)
    obj = SomeModel(**data)
    db.session.add(obj)
    db.session.commit()
    return '201'


@app.route('/delete/', methods=['post'])
def delete_data():
    data = json.loads(request.data)
    obj = Company.query.filter_by(**data).first()
    db.session.delete(obj)
    db.session.commit()
    return '204'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
