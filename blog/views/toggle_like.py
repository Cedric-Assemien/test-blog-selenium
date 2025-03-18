from django.shortcuts import get_object_or_404
from blog.models.article import Article
from blog.models.like import Like
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def toggle_like(request, slug):
    article = get_object_or_404(Article, slug=slug)
    like, created = Like.objects.get_or_create(user=request.user, article=article)

    if not created:
        like.delete()
        return JsonResponse({'message': 'Like supprimé', 'liked': False})
    
    return JsonResponse({'message': 'Article liké', 'liked': True})