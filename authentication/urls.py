from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
	url(r'^login/', views.login, name='login'),
	url(r'^get_last_login/', views.get_last_login, name='get_last_login'),
]