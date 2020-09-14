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

# ---------------------- Generated code block --------------------------------

@api.route('/a')
class get_a(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','a'))

@api.route('/animate')
class get_animate(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','animate'))

@api.route('/animateMotion')
class get_animateMotion(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','animateMotion'))

@api.route('/animateTransform')
class get_animateTransform(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','animateTransform'))

@api.route('/audio')
class get_audio(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','audio'))

@api.route('/canvas')
class get_canvas(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','canvas'))

@api.route('/circle')
class get_circle(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','circle'))

@api.route('/clipPath')
class get_clipPath(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','clipPath'))

@api.route('/defs')
class get_defs(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','defs'))

@api.route('/desc')
class get_desc(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','desc'))

@api.route('/discard')
class get_discard(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','discard'))

@api.route('/ellipse')
class get_ellipse(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','ellipse'))

@api.route('/feBlend')
class get_feBlend(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feBlend'))

@api.route('/feColorMatrix')
class get_feColorMatrix(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feColorMatrix'))

@api.route('/feComponentTransfer')
class get_feComponentTransfer(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feComponentTransfer'))

@api.route('/feComposite')
class get_feComposite(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feComposite'))

@api.route('/feConvolveMatrix')
class get_feConvolveMatrix(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feConvolveMatrix'))

@api.route('/feDiffuseLighting')
class get_feDiffuseLighting(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feDiffuseLighting'))

@api.route('/feDisplacementMap')
class get_feDisplacementMap(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feDisplacementMap'))

@api.route('/feDistantLight')
class get_feDistantLight(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feDistantLight'))

@api.route('/feDropShadow')
class get_feDropShadow(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feDropShadow'))

@api.route('/feFlood')
class get_feFlood(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feFlood'))

@api.route('/feFuncA')
class get_feFuncA(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feFuncA'))

@api.route('/feFuncB')
class get_feFuncB(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feFuncB'))

@api.route('/feFuncG')
class get_feFuncG(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feFuncG'))

@api.route('/feFuncR')
class get_feFuncR(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feFuncR'))

@api.route('/feGaussianBlur')
class get_feGaussianBlur(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feGaussianBlur'))

@api.route('/feImage')
class get_feImage(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feImage'))

@api.route('/feMerge')
class get_feMerge(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feMerge'))

@api.route('/feMergeNode')
class get_feMergeNode(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feMergeNode'))

@api.route('/feMorphology')
class get_feMorphology(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feMorphology'))

@api.route('/feOffset')
class get_feOffset(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feOffset'))

@api.route('/fePointLight')
class get_fePointLight(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','fePointLight'))

@api.route('/feSpecularLighting')
class get_feSpecularLighting(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feSpecularLighting'))

@api.route('/feSpotLight')
class get_feSpotLight(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feSpotLight'))

@api.route('/feTile')
class get_feTile(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feTile'))

@api.route('/feTurbulence')
class get_feTurbulence(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','feTurbulence'))

@api.route('/filter')
class get_filter(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','filter'))

@api.route('/foreignObject')
class get_foreignObject(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','foreignObject'))

@api.route('/g')
class get_g(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','g'))

@api.route('/iframe')
class get_iframe(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','iframe'))

@api.route('/image')
class get_image(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','image'))

@api.route('/line')
class get_line(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','line'))

@api.route('/linearGradient')
class get_linearGradient(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','linearGradient'))

@api.route('/marker')
class get_marker(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','marker'))

@api.route('/mask')
class get_mask(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','mask'))

@api.route('/metadata')
class get_metadata(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','metadata'))

@api.route('/mpath')
class get_mpath(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','mpath'))

@api.route('/path')
class get_path(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','path'))

@api.route('/pattern')
class get_pattern(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','pattern'))

@api.route('/polygon')
class get_polygon(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','polygon'))

@api.route('/polyline')
class get_polyline(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','polyline'))

@api.route('/radialGradient')
class get_radialGradient(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','radialGradient'))

@api.route('/rect')
class get_rect(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','rect'))

@api.route('/script')
class get_script(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','script'))

@api.route('/set')
class get_set(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','set'))

@api.route('/stop')
class get_stop(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','stop'))

@api.route('/style')
class get_style(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','style'))

@api.route('/svg')
class get_svg(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','svg'))

@api.route('/switch')
class get_switch(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','switch'))

@api.route('/symbol')
class get_symbol(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','symbol'))

@api.route('/text')
class get_text(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','text'))

@api.route('/textPath')
class get_textPath(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','textPath'))

@api.route('/title')
class get_title(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','title'))

@api.route('/tspan')
class get_tspan(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','tspan'))

@api.route('/unknown')
class get_unknown(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','unknown'))

@api.route('/use')
class get_use(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','use'))

@api.route('/video')
class get_video(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','video'))

@api.route('/view')
class get_view(Resource):
   def get(self):
      return json.loads(db.execute_command('JSON.GET','view'))

# ---------------------- Generated code block --------------------------------


# Run rest application
if __name__ == '__main__':
    application.run(host='0.0.0.0')
    