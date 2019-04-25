import argparse
import requests
from Game import *

parser = argparse.ArgumentParser()
subs = parser.add_subparsers()

first_parser = subs.add_parser('get_total_score')
first_parser.set_defaults(method='get_total_score')
first_parser.add_argument('--nick', required=True)

second_parser = subs.add_parser('get_max_score')
second_parser.set_defaults(method='get_max_score')
second_parser.add_argument('--nick', required=True)

third_parser = subs.add_parser('run_game')
third_parser.set_defaults(method='run_game')
third_parser.add_argument('--nick', required=True)

args = parser.parse_args()
if args.method == 'get_total_score':
    print(requests.get('http://localhost:50000/get_total_score', json={'nick': args.nick}).json())
elif args.method == 'get_max_score':
    print(requests.get('http://localhost:50000/get_max_score', json={'nick': args.nick}).json())
elif args.method == 'run_game':
    my_game = Game()
    my_game.run()
    print(requests.post('http://localhost:50000/run_game', json={'nick': [args.nick, sum(my_game.list_of_results),
                                                                 max(my_game. list_of_results)]}).json())
