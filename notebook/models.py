from django.db import models

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=500)
    note = models.CharField(max_length=1000)
    
class Word(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    word = models.CharField(max_length=1000)
    pronunciation = models.CharField(max_length=1000)
    note = models.CharField(max_length=1000)
    marked = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    mastered = models.BooleanField(default=False)
    
class Sentence(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    sentence = models.TextField()
    translation = models.TextField()
    marked = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    mastered = models.BooleanField(default=False)