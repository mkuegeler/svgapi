from flask import Flask
from flask_restplus import Resource, Api
import json
from db import db

application = Flask(__name__)

api = Api(application, version='1.0', title='SVG REST API',
    description='This application provides REST access to common SVG elements and their attributes.',
)

# read values from json import file
# def read_json_file(f):
#     # read json file
#     with open(f, "r") as read_file:
#         return json.load(read_file)

# src = read_json_file("data/svg.json")
# svg = src["svg"]

# Connect Redis database and insert sample json
# redis_host = 'redis'
# 
# db = redis.StrictRedis(redis_host, port=6379, db=0)
# db.set('svg', str(svg))
# el = str(db.get('svg').decode('utf-8'))

# db.execute_command('JSON.SET', 'svg', '.', json.dumps(src["svg"]))
# svg = json.loads(db.execute_command('JSON.GET', 'svg'))

@api.route('/svg')
class GetSvg(Resource):
    def get(self):
        return json.loads(db.execute_command('JSON.GET', 'svg'))

@api.route('/rect')
class GetRect(Resource):
    def get(self):
        return json.loads(db.execute_command('JSON.GET', 'rect'))

@api.route('/circle')
class GetCircle(Resource):
    def get(self):
        return json.loads(db.execute_command('JSON.GET', 'circle'))

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    