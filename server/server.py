from flask import Flask
from flask_restplus import Resource, Api
import json
import redis

application = Flask(__name__)
# api = Api(application)
api = Api(application, version='1.0', title='SVG REST API',
    description='This application provides REST access to common SVG elements and their attributes.',
)

# Sample data
# data = {
#     'name': 'svg',
#     'order': 1
# }

el = "node"

# Connect Redis database and insert sample json

redis_host = 'redis'
# db = redis.Redis(host='redis', port=6379, db=0)
db = redis.StrictRedis(redis_host, port=6379, db=0)
# db = redis.Redis(redis_host, socket_connect_timeout=1)
# db = redis.Redis(redis_host)
db.set('element', 'svg')
el = str(db.get('element'))
# el = el[2:]
# el = str(db.keys())

# for key in db.scan_iter():
#     el = el+" - "+key

try:
    db.ping()
    # print('Successfully connected to redis')
    res = 'Successfully connected to redis'
except redis.exceptions.ConnectionError as r_con_error:
    # print('Redis connection error')
    res = 'Redis connection error'
    # handle exception

# db.ping() 
# print('connected to redis "{}"'.format(redis_host)) 


# res = value+test
# db.execute_command('JSON.SET', 'object', '.', json.dumps(data))
# reply = json.loads(db.execute_command('JSON.GET', 'object'))

@api.route('/svg')
class HelloWorld(Resource):
    def get(self):
        return {'key': el}

@api.route('/status')
class HelloStart(Resource):
    def get(self):
        return {'Status': res}

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    