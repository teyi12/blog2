from django.forms import ModelForm
from .models import Article, Profil


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'slug', 'image']




class ProfilForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['photo']
