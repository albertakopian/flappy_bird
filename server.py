import flask
import json
import argparse

app = flask.Flask("FlappyBird")

total_score = {'denis': 17, 'albert': 10, 'bogdan': 19, 'yan': 24, 'misha': 10, 'mehron': 9}
max_score = {'denis': 4, 'albert': 5, 'bogdan': 9, 'yan': 12, 'misha': 5, 'mehron': 5}


@app.route('/get_total_score', methods=['GET'])
def get_total_score():
    print(flask.request.json['nick'])
    return json.dumps(total_score[flask.request.json['nick']])


@app.route('/get_max_score', methods=['GET'])
def get_max_score():
    print(flask.request.json['nick'])
    return json.dumps(max_score[flask.request.json['nick']])


@app.route('/run_game', methods=['POST'])
def run_game():
    total_score[flask.request.json['nick'][0]] = flask.request.json['nick'][1]
    max_score[flask.request.json['nick'][0]] = flask.request.json['nick'][2]
    print(total_score)
    return json.dumps('OK')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50000, type=int)
    args = parser.parse_args()
    app.run('localhost', args.port, debug=True, threaded=True)


if __name__ == '__main__':
    main()
