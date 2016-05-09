from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect 
from notebook.models import Lesson, Word, Sentence

# Create your views here.
def lessons(request):
    """Show a list of all lessons"""
    lessons = Lesson.objects.all()
    print(len(lessons))
    return HttpResponse([x.name for x in lessons])
    
def words(request):
    """Show a list of all words in a lesson"""
    lesson = Lesson.objects.get(pk=request.GET.get("lesson"))
    #words = Word.objects.get(lesson=lesson)
    #words = Lesson.word_set.all()
    words = Word.objects.filter(lesson=lesson)
    
    return HttpResponse([x.word for x in words])
    
def sentences(request):
    """Show a list of all sentences in a lesson"""
    lesson = Lesson.objects.get(pk=request.GET.get("lesson"))
    #sentences = lesson.sentence_set.all()
    sentences = Sentence.objects.filter(lesson=lesson)
    return HttpResponse([x.sentence for x in sentences])

def v1(request):
    Lesson.objects.all().delete()
    
    lesson = Lesson.objects.create(
        name = "A01",
        note = u"初级上 - 01"
    )
    
    word0 = Word.objects.create(
        lesson = lesson,
        word = u"明治",
        pronunciation = u"めいじ",
        note = "Meiji",
        marked = False,
        highlighted = False,
        mastered = False
    )
    
    word1 = Word.objects.create(
        lesson = lesson,
        word = u"昭和",
        pronunciation = u"しょうわ",
        note = "shouwa",
        marked = False,
        highlighted = False,
        mastered = False
    )
    
    sentence0 = Sentence.objects.create(
        lesson = lesson,
        sentence = u"息子がとうとう大学を卒業しました",
        translation = "My son has finally graduted from college.",
        marked = False,
        highlighted = False,
        mastered = False,
    )
    
    return HttpResponse("OK")