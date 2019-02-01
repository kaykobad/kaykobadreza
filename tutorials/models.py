from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Tutorials(models.Model):
    language_name_bn = models.CharField(max_length=100)
    language_name_en = models.CharField(max_length=100)
    slogan_top = models.CharField(max_length=100)
    short_description = models.TextField(max_length=200)
    category = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='uploads/tutorials/', blank=True)

    def __str__(self):
        return self.language_name_bn + " টিউটোরিয়াল"


class TutorialPosts(models.Model):
    language_name_en = models.CharField(max_length=100)
    chapter_no = models.IntegerField()
    chapter_name = models.CharField(max_length=150)
    details = RichTextUploadingField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.language_name_en + " --> " + str(self.chapter_no) + " : " + self.chapter_name