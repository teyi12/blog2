from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    slug = models.SlugField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="articles/", default="default.jpg")

    def __str__(self):
        return self.titre


class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    def __str__(self):
        return self.utilisateur.username


class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    lien = models.URLField(blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titre
