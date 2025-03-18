from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from blog.models.article import Article
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_blog(request):
    articles_list = Article.objects.filter(auteur_id=request.user.id, est_publie=True).order_by("-date_de_publication")
    paginator = Paginator(articles_list, 4)
    
    page = request.GET.get('page',1)
    
    try:
        articles = paginator.get_page(page)
    except InvalidPage:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.get_page(1)

    
    return render(request, 'dashboard_blog.html', {
        "active_dashboard_blog": 'active',
        "articles": articles
    })