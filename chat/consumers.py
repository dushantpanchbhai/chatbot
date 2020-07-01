# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from subprocess import run,PIPE
import sys

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        out=run([sys.executable,"//home//dushant//Desktop//django//chatbot//chatbot//chatbot.py",message],shell=False,stdout=PIPE)
        r=out.stdout
        o=r.decode("utf-8")
        self.send(text_data=json.dumps({
            'message': o,'user':message }))
