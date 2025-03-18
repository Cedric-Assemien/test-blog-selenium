from django.shortcuts import render,redirect,get_object_or_404
from blog.models.article import Article
from blog.forms.article_form import ArticleForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_blog_update(request,slug):
    article = get_object_or_404(Article, slug=slug, auteur_id=request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)  # Ajout de `request.FILES` pour les fichiers
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'create_article.html', {'form': form, "active_create": 'active','title_boutton':'Modifier'})
