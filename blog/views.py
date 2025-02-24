from django.shortcuts import render
from blog.models import Article, Commentaire
from django.core.paginator import Paginator
from blog.forms import CommentaireForm

# Create your views here.

def index(request):
    articles =Article.objects.filter(est_publie=True)[:3]
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
    articles =Article.objects.filter(est_publie=True)
    page_articles = Paginator(articles, 1)
    page_number = request.GET.get("page")
    page_obj = page_articles.get_page(page_number)
    datas = {
        'active_blog' : 'active',
        'articles' : page_obj

    }

    return render(request, 'blog.html', datas)

def blog_details(request, slug):
    form = CommentaireForm()
    article =Article.objects.get(slug=slug)
    if request.method == "POST":
        contenu = request.POST["contenu"]
        
        commentaire = Commentaire()
        commentaire.auteur_id = request.user
        commentaire.article_id = article
        commentaire.contenu = contenu
        commentaire.save()

    datas = {
        'active_blog' : 'active',
        'article':article,
        'comment_form': form
    }

    return render(request, 'blog-single.html', datas)