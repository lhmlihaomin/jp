from django.conf.urls import url
from notebook import views

urlpatterns = [
    url(r'v1/', views.v1, name='v1'),
    url(r'lessons/$', views.lessons, name="lessons"),
    url(r'lessons/add/', views.lessons_add, name="lessons_add"),
    url(r'lessons/delete/', views.lessons_delete, name="lessons_delete"),
    url(r'^lessons/([0-9]+)/words/', views.words, name="words"),
    url(r'^lessons/([0-9]+)/sentences', views.sentences, name="sentences"),
]