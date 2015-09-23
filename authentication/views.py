from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from authentication.models import Application, User, Instance
from utils.functions import *


def index(request):
    return HttpResponse("You're on the home page.")

def register(request):
    context = {}
    if request.method == 'GET':
        #print(list(request.GET))
        var = list(request.GET)[0].replace('\'','')
        #print(var)
        try:
            data = json.loads(var)
            app_id = data['app_id']
            email = data['email']
            name_surname = data['name_surname'] 
            password = data['password']
            #print(data["app_id"])
            if Application.objects.filter(app_id=app_id).exists():
                if not User.objects.filter(email=email).exists():
                    token = token_generator()
                    context['token'] = token
                    user = save_user(email, name_surname, password)
                    create_instance(user, token, app_id)
                    context['code'] = 0
                else:
                    context['code'] = 1
            else:
                context['code'] = 2
        except ValueError:
            print('Json fail')
            context['code'] = 2
    return JsonResponse(context)

def login(request):
    context = {}
    if request.method == 'GET':
        var = list(request.GET)[0].replace('\'', '')
        try:
            data = json.loads(var)
            app_id = data['app_id']
            email = data['email']
            password = data['password']
            if Application.objects.filter(app_id=app_id).exists():
                if User.objects.filter(email=email, password=password).exists():
                    token = token_generator()
                    context['code'] = 0
                    context['token'] = token
                    instance = Instance.objects.filter(user__email=email, app_id=app_id)[0]
                    update_instance(instance, token, app_id, email)
                else:
                    print(User.objects.filter(email=email))
                    context['code'] = 2
            else:
                context['code'] = 2
        except ValueError:
            print('JSON fail')
            context['code'] = 2
    else:
        context['code'] = 2
    return JsonResponse(context)

def get_last_login(request):
    context = {}
    if request.method == 'GET':
        #print(list(request.GET))
        var = list(request.GET)[0].replace('\'','')
        #print(var)
        try:
            data = json.loads(var)
            app_id = data['app_id']
            token = data['token']
            email = data['email']
            if Application.objects.filter(app_id=app_id).exists():
                if User.objects.filter(email=email).exists():
                    if Instance.objects.filter(token=token).exists():
                        context['code'] = 0
                        context['time'] = Instance.objects.filter(token=token)[0].time.strftime("%H:%M:%S, %B %d, %Y")
                    else:
                        context['code'] = 3
                else:
                    context['code'] = 2
            else:
                context['code'] = 2
        except ValueError:
            print('JSON fail')
            context['code'] = 2
    else:
        context['code'] = 2
    return JsonResponse(context)

