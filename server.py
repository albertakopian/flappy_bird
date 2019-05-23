import flask
import json
import argparse
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask("FlappyBird")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class gamer(db.Model):
    def __init__(self, username, total_score, max_score):
        self.username = username
        self.total_score = total_score
        self.max_score = max_score

    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    max_score = db.Column(db.Integer, nullable=True)
    total_score = db.Column(db.Integer, nullable=True)


db.create_all()


@app.route('/get_total_score', methods=['GET'])
def get_total_score():
    user = gamer.query.filter_by(username=flask.request.json['nick']).first()
    return json.dumps(user.total_score)


@app.route('/get_max_score', methods=['GET'])
def get_max_score():
    user = gamer.query.filter_by(username=flask.request.json['nick']).first()
    return json.dumps(user.max_score)


@app.route('/run_game', methods=['POST'])
def run_game():
    db.session.add(gamer(flask.request.json['nick'][0], flask.request.json['nick'][1], flask.request.json['nick'][2]))
    db.session.commit()
    return json.dumps('OK')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=50000, type=int)
    args = parser.parse_args()
    app.run(args.host, args.port, debug=True, threaded=True)


if __name__ == '__main__':
    main()
