from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from line_bot_ai.line_message import LineMessage

"""
@csrf_exempt
def index(request):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        line_message.reply(reply_token)
        return HttpResponse("ok")
"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

