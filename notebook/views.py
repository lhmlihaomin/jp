# coding=utf8
import re
import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
 
from notebook.models import Lesson, Word, Sentence

# Create your views here.
def lessons(request):
    """Show a list of all lessons"""
    title = "Lessons List"
    # get and sort all lessons:
    lessons = Lesson.objects.order_by("name")
    # increment the last lesson name by "1" as the new default name:
    if len(lessons) > 0:
        last_lesson_name = lessons[len(lessons)-1].name
        p = "([a-zA-Z]+)(\d+)"
        m = re.match(p, last_lesson_name)
        if m is not None:
            order_len = len(m.groups()[1])
            new_order = int(m.groups()[1]) + 1
            fmt = "%s%0"+str(order_len)+"d"
            new_name = fmt%(m.groups()[0], new_order)
        else:
            new_name = "A01"
    
    return render(request, "notebook/lessons.html", locals())
    
def lessons_add(request):
    """Add a lesson."""
    name = request.POST.get("new_lesson_name").strip()
    note = request.POST.get("new_lesson_note").strip()
    
    p = "([a-zA-Z]+)(\d+)"
    m = re.match(p, name)
    if len(name) == 0 or m is None:
        return HttpResponse("Invalid lesson name.")
    lesson = Lesson.objects.create(
        name = name,
        note = note
    )
    return HttpResponseRedirect(reverse("lessons"))
    
def lessons_delete(request):
    """Delete one or multiple lessons"""
    lesson_ids = request.POST.getlist("lesson_id[]")
    lessons = Lesson.objects.filter(pk__in=lesson_ids)
    if len(lessons) > 0:
        for i in range(len(lessons)):
            lessons[i].delete()
    return HttpResponseRedirect("../")
    
def words(request, index):
    """Show a list of all words in a lesson"""
    lesson = Lesson.objects.get(pk=int(index))
    title = "Words - "+lesson.name
    words = Word.objects.filter(lesson=lesson)
    
    #return HttpResponse([x.word for x in words])
    return render(request, "notebook/words.html", locals())
    
def words_add(request):
    """Add one or multiple words to a lesson."""
    title = "Add Words"
    lessons = Lesson.objects.all()
    if request.method.lower() == "post":
        lesson = Lesson.objects.get(pk=request.POST.get('lesson'))
        words = request.POST.getlist('word[]')
        pronuns = request.POST.getlist('pronunciation[]')
        notes = request.POST.getlist('note[]')
        
        for i, word in enumerate(words):
            if len(words[i].strip()) == 0:
                continue
            word = Word.objects.create(
                word=words[i],
                pronunciation=pronuns[i],
                note=notes[i],
                marked=False,
                highlighted=False,
                mastered=False,
                lesson=lesson
            )
        
    return render(request, "notebook/words_add.html", locals())
    
def words_delete(request):
    pass
    
def word_mark(request):
    word_id = request.GET.get('id')
    try:
        word = Word.objects.get(pk=word_id);
        word.marked = not word.marked
        word.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(word.marked))
    
def word_highlight(request):
    word_id = request.GET.get('id')
    try:
        word = Word.objects.get(pk=word_id);
        word.highlighted = not word.highlighted
        word.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(word.highlighted))
    
def word_mastered(request):
    word_id = request.GET.get('id')
    try:
        word = Word.objects.get(pk=word_id);
        word.mastered = not word.mastered
        word.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(word.mastered))
    
def sentences(request, index):
    """Show a list of all sentences in a lesson"""
    lesson = Lesson.objects.get(pk=int(index))
    title = "Sentences - "+lesson.name
    sentences = Sentence.objects.filter(lesson=lesson)
    
    #return HttpResponse([x.sentence for x in sentences])
    return render(request, "notebook/sentences.html", locals())

def sentences_add(request):
    """Add one or multiple sentences to a lesson."""
    title = "Add Sentences"
    lessons = Lesson.objects.all()
    if request.method.lower() == "post":
        lesson = Lesson.objects.get(pk=request.POST.get('lesson'))
        sentences = request.POST.getlist('sentence[]')
        translations = request.POST.getlist('translation[]')
        
        for i, sentence in enumerate(sentences):
            if len(sentence[i].strip()) == 0:
                continue
            sentence = Sentence.objects.create(
                sentence=sentences[i],
                translation=translations[i],
                marked=False,
                highlighted=False,
                mastered=False,
                lesson=lesson
            )
        
    return render(request, "notebook/sentences_add.html", locals())

def sentence_mark(request):
    sentence_id = request.GET.get('id')
    try:
        sentence = Sentence.objects.get(pk=sentence_id);
        sentence.marked = not sentence.marked
        sentence.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(sentence.marked))
    
def sentence_highlight(request):
    sentence_id = request.GET.get('id')
    try:
        sentence = Sentence.objects.get(pk=sentence_id);
        sentence.highlighted = not sentence.highlighted
        sentence.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(sentence.highlighted))
    
def sentence_mastered(request):
    sentence_id = request.GET.get('id')
    try:
        sentence = Sentence.objects.get(pk=sentence_id);
        sentence.mastered = not sentence.mastered
        sentence.save()
    except Exception as ex:
        return HttpResponse(ex.message, status=500)
    return HttpResponse(json.dumps(sentence.mastered))
    
def words_allmarked(request):
    """List all marked words."""
    words = Word.objects.filter(marked=True)
    return render(request, "notebook/words_allmarked.html", locals())
    
def sentences_allmarked(request):
    """List all marked sentences."""
    sentences = Sentence.objects.filter(marked=True)
    return render(request, "notebook/sentences_allmarked.html", locals())
    
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
    
def v2(request):
    lessons = Lesson.objects.all()
    print(request.method)
    if request.method.lower() == "post":
        lesson = Lesson.objects.get(pk=request.POST.get('lesson'))
        words = request.POST.getlist('word[]')
        pronuns = request.POST.getlist('pronunciation[]')
        notes = request.POST.getlist('note[]')
        
        for i, word in enumerate(words):
            word = Word.objects.create(
                word=words[i],
                pronunciation=pronuns[i],
                note=notes[i],
                marked=False,
                highlighted=False,
                mastered=False,
                lesson=lesson
            )
        
    return render(request, "notebook/v2.html", locals())
    