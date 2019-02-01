from django.contrib import admin
from .models import Questions, PendingQuestion

# Register your models here.

admin.site.register(Questions)
admin.site.register(PendingQuestion)