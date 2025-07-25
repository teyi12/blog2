from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from blog import views, views_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Pages principales
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('remerciement/', views.remerciement_view, name='remerciement'),

    # Articles app
    path('articles/', include('articles.urls')),

    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views_auth.signup_view, name='signup'),

    # Profil utilisateur
    path('profil/', views_auth.profil_view, name='profil'),
    path('profil/modifier/', views_auth.modifier_profil, name='modifier_profil'),
    path('services/', views.services_view, name='services'),
    path('a-propos/', views.a_propos_view, name='a_propos'),
    path('a-propos/', views.a_propos_view, name='a_propos'),
    path('portfolio/', TemplateView.as_view(template_name="portfolio.html"), name='portfolio'),
    path('', include('articles.urls')),  # ou l'app où tu places tes projets


]

# Pour servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()