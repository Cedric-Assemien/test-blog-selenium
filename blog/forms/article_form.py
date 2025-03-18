from django import forms
from blog.models.article import Article
from blog.models.categorie import Categorie
from blog.models.tag import Tag
from datetime import date
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget(attrs={'id': 'contenu'}))

    class Meta:
        model = Article
        fields = ['titre', 'couverture', 'resume' , 'categorie_id', 'tag_ids','contenu']
        widgets = {
            'titre': forms.TextInput(attrs={
                "type": "text",
                "name": "titre",
                "class": "form-control",
                "id": "titre",
                "placeholder": "titre*"
                }),
            'couverture': forms.FileInput(attrs={
                "name": "couverture",
                "class": "form-control",
                "id": "couverture",
                "placeholder": "couverture*"
                }),
            'tag_ids': forms.SelectMultiple(attrs={
                "name": "tags",
                "class": 'form-control',
                "id": "tags",
                "placeholder": "tags*"
                }),
            'categorie_id': forms.Select(attrs={
                "name": "categorie",
                "class": 'form-control',
                "id": "categorie_id",
                "placeholder": "categorie_id*",
                "title": "categorie"
                }),
            'resume': forms.Textarea(attrs={
                "name": "resumé",
                "class": 'form_control',
                "id": "resume",
                "rows":"4",
                "placeholder": "votre resumé...*",
                "title": "tag"
                }),
            'contenu' : forms.CharField(
                widget=CKEditorWidget(
                    attrs={'id': 'contenu'}
                )
                ),
        }

    def clean_titre(self):
        """ Vérifie si un article avec ce titre existe déjà. """
        titre = self.cleaned_data['titre']
        if Article.objects.filter(titre=titre).exists():
            raise ValidationError("Un article avec ce titre existe déjà. Veuillez choisir un autre titre.")
        return titre

    def clean_categorie_id(self):
        """ Vérifie si la catégorie existe, sinon elle est créée. """
        categorie = self.cleaned_data['categorie_id']
        if not Categorie.objects.filter(nom=categorie.nom).exists():
            categorie.save()
        return categorie

    def clean_tag_ids(self):
        """ Vérifie si chaque tag existe, sinon il est créé. """
        tags = self.cleaned_data['tag_ids']
        for tag in tags:
            if not Tag.objects.filter(nom=tag.nom).exists():
                tag.save()
        return tags

    def clean_couverture(self):
        couverture = self.cleaned_data.get('couverture')
        if not couverture:
            raise forms.ValidationError("Veuillez ajouter une image de couverture.")
        return couverture

    def save(self, commit=True):
        """ Définit automatiquement la date de publication et force `est_publie` à False. """
        article = super().save(commit=False)
        article.date_de_publication = date.today()  
        article.est_publie = True 

        if commit:
            article.save()
            self.save_m2m()  

        return article