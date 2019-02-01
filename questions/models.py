from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Questions(models.Model):
    question_text = models.CharField(max_length=300)
    question_answer = RichTextField()
    question_owner = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.question_text[:30]


class PendingQuestion(models.Model):
    author = models.CharField(max_length=150)
    email = models.EmailField()
    date = models.DateTimeField()
    text_details = models.TextField()

    def __str__(self):
        return self.author + " --> " + self.text_details[:30]