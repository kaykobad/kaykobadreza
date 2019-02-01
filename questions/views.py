from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import Questions, PendingQuestion
from django.utils import timezone


# Create your views here.


def questions(request):
    try:
        questions = Questions.objects.all()
        return render(request, 'questionanswer/questionanswer.html', {
            'questions': questions,
            'pagename': 'questions',
        })
    except:
        warning = "Questions answers will be available soon!!!"
        return render(request, 'questionanswer/questionanswer.html', {
            'warning': warning,
            'pagename': 'questions',
        })


def ask_question(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']
        date = timezone.now()

        new_entry = PendingQuestion(author=name, email=email, text_details=comments, date=date)
        new_entry.save()

        return render(request, 'questionanswer/askquestion.html', {
            'message': 'আপনার প্রশ্নটি সংরক্ষণ করা হয়েছে।',
            'pagename': 'askquestions',
        })

    return render(request, 'questionanswer/askquestion.html', {'pagename': 'askquestions',})


def specific_question(request, question_id):
    try:
        questions = Questions.objects.get(pk=question_id)
        #return HttpResponse("Got em..")
        return render(request, 'questionanswer/questionanswer.html', {
            'questions': questions,
            'single': "true",
            'pagename': 'questions',
        })
    except Exception as ex:
        warning = "দুঃখিত! আপনার প্রশ্নটি ডাটাবেসে পাওয়া যায়নি।"
        return render(request, 'questionanswer/questionanswer.html', {
            'warning': warning,
            'pagename': 'questions',
        })

