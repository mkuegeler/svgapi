from flask import Flask
from flask_restplus import Resource, Api

application = Flask(__name__)
# api = Api(application)
api = Api(application, version='1.0', title='SVG REST API',
    description='This application provides REST access to common SVG elements and their attributes.',
)

@api.route('/svg')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'svg'}

@api.route('/dev')
class HelloStart(Resource):
    def get(self):
        return {'hello': 'dev'}

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    