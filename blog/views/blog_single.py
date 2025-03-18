from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from blog.models.article import Article
from blog.models.commentaire import Commentaire


def blog_single(request,slug):
    article = Article.objects.get(slug = slug)
    commentaires =Commentaire.objects.filter(article_id=article)
    paginator = Paginator(commentaires, 3)
    
    page = request.GET.get('page',1)
    
    try:
        commentaires = paginator.get_page(page)
    except InvalidPage:
        commentaires = paginator.page(1)
    except EmptyPage:
        commentaires = paginator.get_page(1)

    datas = {
        "article" : article,
        "commentaires" : commentaires
    }

    return render(request, 'blog-single.html', datas)