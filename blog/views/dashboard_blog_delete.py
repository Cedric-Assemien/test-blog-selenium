from django.shortcuts import redirect, get_object_or_404
from blog.models.article import Article

def dashboard_blog_delete(request, slug):
    article = get_object_or_404(Article, slug=slug, auteur_id=request.user)

    article.est_publie = False
    article.save()

    return redirect('dashboard_blog')