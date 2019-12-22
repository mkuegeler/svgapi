# Connect to Redis database
import json
import redis

# read values from json import file
def read_json_file(f):
    # read json file
    with open(f, "r") as read_file:
        return json.load(read_file)

redis_host = 'redis'
import_file = "data/svg.json"
src = read_json_file(import_file)

db = redis.StrictRedis(redis_host, port=6379, db=0)

for key,value in src.items():
   db.execute_command('JSON.SET', key, '.', json.dumps(value))