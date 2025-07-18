from django import forms
from django.contrib.auth.models import User
from .models import Article, Profil


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'slug', 'image']


class ProfilForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="Prénom", max_length=100, required=False)
    last_name = forms.CharField(label="Nom", max_length=100, required=False)

    class Meta:
        model = Profil
        fields = ['photo']  # Uniquement le champ du modèle Profil

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['email'].initial = self.user.email
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name

    def save(self, commit=True):
        profil = super().save(commit=False)

        if self.user:
            self.user.email = self.cleaned_data['email']
            self.user.first_name = self.cleaned_data['first_name']
            self.user.last_name = self.cleaned_data['last_name']
            if commit:
                self.user.save()
                profil.utilisateur = self.user
                profil.save()
        return profil
