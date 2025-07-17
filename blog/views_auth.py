from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from articles.forms import ProfilForm
from articles.models import Profil


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Créer un profil automatiquement
            Profil.objects.create(utilisateur=user)
            login(request, user)
            return redirect('profil')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profil_view(request):
    profil, created = Profil.objects.get_or_create(utilisateur=request.user)
    return render(request, 'users/profil.html', {'profil': profil})


@login_required
def modifier_profil(request):
    profil, created = Profil.objects.get_or_create(utilisateur=request.user)

    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = ProfilForm(instance=profil)

    return render(request, 'users/modifier_profil.html', {'form': form})
