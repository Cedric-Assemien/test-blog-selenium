from django.shortcuts import render,redirect
from blog.forms.article_form import ArticleForm
from django.contrib.auth.decorators import login_required


@login_required
def creer_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur_id = request.user
            article.save()
            form.save_m2m()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form, "active_create": 'active','title_boutton':'Créer article'})
