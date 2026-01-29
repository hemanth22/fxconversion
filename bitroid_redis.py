import redis
import os

host = os.environ.get('REDIS_HOST')
port = os.environ.get('REDIS_PORT')
username = os.environ.get('REDIS_USERNAME')
password = os.environ.get('REDIS_PASSWORD')

r = redis.Redis(host=host,port=port,decode_responses=True,username=username,password=password)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

