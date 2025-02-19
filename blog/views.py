from django.shortcuts import render
from blog.models import Article

# Create your views here.

def index(request):
    articles =Article.objects.filter(est_publie=True)
    datas = {
        'active_index' : 'active',
        'articles' : articles,
    }

    return render(request, 'index.html', datas)

def contact(request):
    datas = {
        'active_contact' : 'active'

    }

    return render(request, 'contact.html', datas)

def about(request):
    datas = {
        'active_about' : 'active'

    }

    return render(request, 'about.html', datas)

def blog(request):
    datas = {
        'active_blog' : 'active'

    }

    return render(request, 'blog.html', datas)

def blog_details(request, pk):
    article =Article.objects.get(pk=pk)

    datas = {
        'active_blog' : 'active',
        'article':article,

    }

    return render(request, 'blog-single.html', datas)