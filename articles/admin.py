from django.contrib import admin
from .models import Article, Profil
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
    list_select_related = ('utilisateur',)  # Optimise la requête

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
