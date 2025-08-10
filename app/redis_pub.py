import redis
import psutil
import time
import json
from config.redis_config import REDIS_CONFIG

r = redis.Redis(**REDIS_CONFIG)

while True:
    data = {
        'cpu': psutil.cpu_percent(),
        'ram': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    r.publish('real_time_dashboard', json.dumps(data))
    print(data)
    time.sleep(1)
