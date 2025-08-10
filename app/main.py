import asyncio
import tornado.websocket
import tornado.web
from websocket_handler import WebSocketHandler, connected_clients
from redis_listener import listener_redis

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WebSocketHandler),
    ], 
    template_path="templates/",
    static_path="static/")

async def broadcast_to_clients(data):
    if connected_clients:
        clients_copy = connected_clients.copy()
        
        for client in clients_copy:
            try:
                if hasattr(client, 'write_message'):
                    client.write_message(data)
            except Exception as e:
                print(f"Erro ao enviar mensagem para cliente: {e}")
                connected_clients.discard(client)

async def handle_redis_message(data):
    print(f"Processando mensagem do Redis: {data}")

    await broadcast_to_clients(data)

async def main():
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    print("Server rodando")
    print("Interface web em: http://localhost:8888")
    
    redis_task = asyncio.create_task(listener_redis(handle_redis_message))
    
    try:
        await asyncio.Event().wait()
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
        redis_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())