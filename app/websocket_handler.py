import tornado.websocket
import json

connected_clients = set()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        connected_clients.add(self)
        print(f"Nova conexão WebSocket. Total de clientes: {len(connected_clients)}")
        
        welcome_msg = {
            "type": "connection",
            "message": "Conectado ao dashboard em tempo real",
            "timestamp": str(self.get_current_time())
        }
        self.write_message(json.dumps(welcome_msg))

    def on_close(self):
        connected_clients.discard(self)
        print(f"Conexão WebSocket fechada. Total de clientes: {len(connected_clients)}")
    
    def on_message(self, message):
        print(f"Mensagem recebida do cliente: {message}")
    
    def check_origin(self, origin):
        return True
    
    def get_current_time(self):
        import datetime
        return datetime.datetime.now().isoformat()