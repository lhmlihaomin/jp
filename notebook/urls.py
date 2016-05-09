from django.conf.urls import url
from notebook import views

urlpatterns = [
    url(r'v1/', views.v1, name='v1'),
    url(r'lessons/', views.lessons, name="lessons"),
    url(r'^words/', views.words, name="words"),
    url(r'^sentences/', views.sentences, name="sentences"),
]