from django.conf.urls import url
from notebook import views

urlpatterns = [
    url(r'v1/', views.v1, name='v1'),
    url(r'v2/', views.v2, name='v2'),
    url(r'lessons/$', views.lessons, name="lessons"),
    url(r'lessons/add/', views.lessons_add, name="lessons_add"),
    url(r'lessons/delete/', views.lessons_delete, name="lessons_delete"),
    url(r'^lessons/([0-9]+)/words/$', views.words, name="words"),
    url(r'^words_add/$', views.words_add, name="words_add"),
    url(r'^lessons/[0-9]+/words/mark/', views.word_mark, name="word_mark"),
    url(r'^lessons/[0-9]+/words/highlight/', views.word_highlight, name="word_highlight"),
    url(r'^lessons/[0-9]+/words/mastered/', views.word_mastered, name="word_mastered"),
    url(r'^words_allmarked/', views.words_allmarked, name="words_allmarked"),
    url(r'^lessons/([0-9]+)/sentences/$', views.sentences, name="sentences"),
    url(r'^sentences_add/$', views.sentences_add, name="sentences_add"),
    url(r'^lessons/[0-9]+/sentences/mark/', views.sentence_mark, name="sentence_mark"),
    url(r'^lessons/[0-9]+/sentences/highlight/', views.sentence_highlight, name="sentence_highlight"),
    url(r'^lessons/[0-9]+/sentences/mastered/', views.sentence_mastered, name="sentence_mastered"),
    url(r'^sentences_allmarked/', views.sentences_allmarked, name="sentences_allmarked")
]