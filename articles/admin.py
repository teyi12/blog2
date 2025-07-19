from django.contrib import admin
from .models import Article, Profil, Projet
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'slug', 'date_publication')
    search_fields = ('titre', 'slug')
    list_filter = ('date_publication',)
    prepopulated_fields = {'slug': ('titre',)}


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('lien_utilisateur', 'afficher_photo')
    list_select_related = ('utilisateur',)

    def afficher_photo(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />',
                obj.photo.url
            )
        return "Aucune"
    afficher_photo.short_description = "Photo"
    afficher_photo.admin_order_field = 'photo'

    def lien_utilisateur(self, obj):
        url = reverse("admin:auth_user_change", args=[obj.utilisateur.id])
        return format_html('<a href="{}">{}</a>', url, obj.utilisateur.username)
    lien_utilisateur.short_description = "Utilisateur"

# ✅ Nouveau : affichage admin pour Projet
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'afficher_image', 'lien')
    search_fields = ('titre', 'description')
    list_filter = ('date_creation',)
    readonly_fields = ('date_creation',)

    def afficher_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="40" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "Pas d'image"
    afficher_image.short_description = "Image"
