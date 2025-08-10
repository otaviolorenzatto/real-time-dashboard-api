import redis
import asyncio
from config.redis_config import REDIS_CONFIG

r = redis.Redis(**REDIS_CONFIG)
pubsub = r.pubsub()
pubsub.subscribe('real_time_dashboard')

async def listener_redis(callback):
    print("Iniciando leitura de mensagens do Redis...")
    
    try:
        for message in pubsub.listen():
            if message and message['type'] == 'message':
                data = message['data']
                if callback:
                    await callback(data)
        
            await asyncio.sleep(0.1)
        
    except Exception as e:
        print(f"Erro no Redis listener : {e}")
        await asyncio.sleep(1)