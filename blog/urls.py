
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views_auth import signup_view, profil_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views_auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('remerciement/', views.remerciement_view, name='remerciement'),
    path('articles/', include('articles.urls'), name='articles'),
    
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
   
    path('logout/', LogoutView.as_view(next_page='login', http_method_names=['get', 'post']), name='logout'),

    path('signup/', signup_view, name='signup'),
    path('profil/', profil_view, name='profil'),
    path('profil/modifier/', views_auth.modifier_profil, name='modifier_profil'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
