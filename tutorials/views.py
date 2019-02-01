from django.shortcuts import render
from .models import TutorialPosts, Tutorials

# Create your views here.


def tutorials(request):
    try:
        tutorial_list = Tutorials.objects.all()
        return render(request, 'tutorials/tutorials.html', {
            'tutorial_list': tutorial_list,
            'pagename': 'tutorials',
        })
    except:
        warning = "Tutorials will be available soon!!!"
        return render(request, 'tutorials/tutorials.html', {
            'warning': warning,
            'pagename': 'tutorials',
        })


def tut_details(request, tutname, chapter=0):
    prev = next = 0
    all_posts = []
    language  = ""
    try:
        all_posts = TutorialPosts.objects.filter(language_name_en=tutname)
        slogan = Tutorials.objects.get(language_name_en=tutname)
        language = slogan.language_name_bn
        slogan = slogan.slogan_top

        post = TutorialPosts.objects.get(chapter_no=chapter)

        min = 0
        max = len(all_posts) - 1

        if chapter == min:
            prev = 0
            next = 1
        elif max == chapter:
            prev = max - 1
            next = 0
        else:
            prev = chapter - 1
            next = chapter + 1

        return render(request, 'tutorials/tutorialdetails.html', {
            'language': language,
            'index': all_posts,
            'post': post,
            'name': tutname,
            'slogan': slogan,
            'prev': prev,
            'next': next,
            'pagename': 'tutorials',
        })
    except Exception as ex:
        #return HttpResponse(str(ex))
        return render(request, 'tutorials/tutorialdetails.html', {
            'language': language,
            'index': all_posts,
            'message': 'দুঃখিত, এই টিউটোরিয়াল/পোষ্টটি ডাটাবেস থেকে পাওয়া যায়নি।',
            'name': tutname,
            'slogan': '',
            'prev': prev,
            'next': next,
            'pagename': 'tutorials',
        })