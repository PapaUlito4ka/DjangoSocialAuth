from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from social_app.settings import SECRET_KEY
from core.models import Message
import core.api_requests as api

import json


def login(request):
    return render(request, 'login.html')


def home(request):
    context = {
        'last_message': api.get_last_message(),
        'user_id': request.session['_auth_user_id'] if '_auth_user_id' in request.session else 0
    }
    return render(request, 'home.html', context)


@csrf_exempt
@require_http_methods(['POST'])
def send_message(request):
    if request.headers['token'] == SECRET_KEY:
        data = json.loads(request.body.decode('utf-8'))
        message = Message(
            user_id=data['user_id'],
            text=data['text']
        )
        try:
            message.save()
        except Exception as e:
            data = { 'message': e.__str__() }
            return JsonResponse(data, status=404, content_type='application/json')
        data = {
            'message': 'ok'
        }
        return JsonResponse(data, status=200, content_type='application/json')


@require_http_methods(['GET'])
def last_message(request):
    if request.headers['token'] == SECRET_KEY:
        if len(Message.objects.all()) == 0:
            data = {
                'data': 'No messages'
            }
        else:
            message = Message.objects.last()
            data = {
                'data': {
                    'text': message.text,
                    'user': message.user.first_name,
                    'send_at': message.send_at.strftime("%d.%m.%Y %H:%M:%S"),
                    'bro_message_cnt': len(Message.objects.filter(text='Bro!').all()),
                    'sis_message_cnt': len(Message.objects.filter(text='Sis!').all())
                }
            }
        return JsonResponse(data, status=200, content_type='application/json')
