from blog.models.article import Article
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def liked_articles(request):
    articles = Article.objects.filter(likes__user=request.user)
    data = [{"id": article.id, "title": article.titre, "content": article.contenu} for article in articles]
    
    return JsonResponse({'liked_articles': data})
