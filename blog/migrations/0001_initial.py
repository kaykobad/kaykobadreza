# Generated by Django 2.1.2 on 2018-10-29 02:56

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_author', models.CharField(max_length=100)),
                ('post_title', models.CharField(max_length=200)),
                ('bannar_img', models.ImageField(upload_to='')),
                ('post_details', ckeditor_uploader.fields.RichTextUploadingField()),
                ('pub_date', models.DateField()),
                ('total_visits', models.BigIntegerField(default=0)),
            ],
        ),
    ]
