from django.db import models

class Application(models.Model):
    app_id = models.CharField(max_length=20, unique=True, primary_key=True)

    def __str__(self):
        return self.app_id

class User(models.Model):
    email = models.CharField(max_length=50)
    name_surname = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
        
    def __str__(self):
        return self.name_surname + ' ' + self.password

class Instance(models.Model):
    token = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    app = models.ForeignKey(Application)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email + ' ' + self.token

   

   #localhost:8000/register?'{"app_id":"0", "email":"email1@gmail.com", "name_surname":"melnic ion", "password":"1234"}'
   #localhost:8000/login?'{"app_id":"0", "email":"email1@gmail.com", "password":"1234"}'
   #localhost:8000/get_last_login?'{"app_id":"2", "token":"G1001skhzV", "email":"email111@gmail.com"}'