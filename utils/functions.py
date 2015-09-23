import random, string, datetime
from authentication.models import Instance, Application, User

def token_generator():
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    token = ''.join(random.SystemRandom().choice(symbols) for x in range(20))
    return token

def create_instance(user, token, app_id):
    instance = Instance(user=user, token=token, app_id=app_id, time=datetime.date.today())
    instance.save()
    return

def save_user(email, name_surname, password):
    user = User(email=email, name_surname= name_surname, password=password)
    user.save()
    return user

def update_instance(instance, token, app_id, email):
    user = User.objects.filter(email=email)[0]
    instance.token = token
    instance.user = user
    instance.app_id = app_id
    instance.save()
    return