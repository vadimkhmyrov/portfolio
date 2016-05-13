from django.conf.urls import url

from . import views

app_name = 'pokerclock'
urlpatterns = [
    url(r'^create/$', views.create_game, name='main'),
    url(r'^game/$', views.start_game, name='game'),
]
