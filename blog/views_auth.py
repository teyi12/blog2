from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profil')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

@login_required
def profil_view(request):
    return render(request, 'auth/profil.html')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from articles.forms import ProfilForm

@login_required
def modifier_profil(request):
    profil = request.user.profil  # via OneToOneField

    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            return redirect('profil')  # ou autre nom de page profil
    else:
        form = ProfilForm(instance=profil)

    return render(request, 'modifier_profil.html', {'form': form})
