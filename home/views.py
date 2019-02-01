from django.shortcuts import render
from .models import Subscriber
from django.utils import timezone


def home(request):

    if request.method == 'POST':
        # get the email address
        email = request.POST['subscriber_mail']

        # check for duplicate entry
        try:
            duplicate = Subscriber.objects.get(email_address=email)
        except:
            entry_email = Subscriber(email_address=email, date=timezone.now())
            entry_email.save()
        
        return render(request, 'home/home.html', {
            'message': 'আপনি সফলভাবে সাবস্ক্রাইব করেছেন',
            'pagename': 'home',
        })

    return render(request, 'home/home.html', {'pagename': 'home',})
