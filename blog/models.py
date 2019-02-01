from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    post_author = models.CharField(max_length=100)
    post_title = models.CharField(max_length=200)
    bannar_img = models.ImageField()
    post_details = RichTextUploadingField()
    pub_date = models.DateField()
    total_visits = models.BigIntegerField(default=0)

    def __str__(self):
        return self.post_title
