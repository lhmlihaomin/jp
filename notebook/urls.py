from django.conf.urls import url
from notebook import views

urlpatterns = [
    url(r'v1/', views.v1, name='v1'),
    url(r'lessons/$', views.lessons, name="lessons"),
    url(r'lessons/add/', views.lessons_add, name="lessons_add"),
    url(r'^words/([0-9]+)/', views.words, name="words"),
    url(r'^sentences/([0-9]+)/', views.sentences, name="sentences"),
]