from django.contrib import admin
from .models import Article, Profil
from django.utils.html import mark_safe

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'afficher_photo')  # colonnes visibles
    list_select_related = ('utilisateur',)  # optimisation des requêtes

    def afficher_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 50%;">')
        return "Aucune"
    afficher_photo.short_description = "Photo"
    afficher_photo.allow_tags = True
    afficher_photo.admin_order_field = 'photo'
    afficher_photo.allow_tags = True

admin.site.register(Article)
