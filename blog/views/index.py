from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from blog.models.article import Article


def index(request):
    articles_list = Article.objects.filter(est_publie=True).order_by("-date_de_publication")
    paginator = Paginator(articles_list, 6)
    
    page = request.GET.get('page',1)
    
    try:
        articles = paginator.get_page(page)
    except InvalidPage:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.get_page(1)

    datas = {
        "articles": articles,
        "active_index": 'active'
    }

    return render(request, 'index.html', datas)