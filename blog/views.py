from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.

def blog_home(request):
    all_posts = BlogPost.objects.all().order_by('pub_date')
    recent_posts = all_posts[:5]

    # get the post
    if request.method == 'POST':
        item_searched = request.POST['search'].lower()
        try:
            all_posts = [post for post in all_posts if (post.post_title+post.post_author+post.post_details).lower().find(item_searched) != -1]
        except Exception as ex:
            return HttpResponse(ex)

    for i in range(len(all_posts)):
        all_posts[i].post_details = all_posts[i].post_details[3:120]+'...'

    return render(request, 'blog/bloghome.html', {
        'all_posts': all_posts,
        'pagename': 'blog',
        'recent_posts': recent_posts,
    })


def show_post(request, post_id):
    all_posts = BlogPost.objects.all().order_by('pub_date')
    recent_posts = all_posts[:5]
    try:
        post = BlogPost.objects.get(pk=post_id)
        return render(request, 'blog/bloghome.html', {
            'post': post,
            'single': True,
            'pagename': 'blog',
            'recent_posts': recent_posts,
        })
    except:
        return render(request, 'blog/bloghome.html', {
            'warning': "দুঃখিত! আপনার পোষ্টটি ডাটাবেসে পাওয়া যায়নি।",
            'pagename': 'blog',
            'recent_posts': recent_posts,
        })