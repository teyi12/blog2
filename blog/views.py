from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def home_view(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Objet et contenu du mail
            sujet = f"Blog | Contact de {nom} {prenom}"
            contenu = f"Email: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    sujet,
                    contenu,
                    settings.DEFAULT_FROM_EMAIL,  # à configurer dans settings.py
                    [settings.CONTACT_EMAIL],     # à configurer aussi
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Erreur lors de l'envoi du mail: {e}")
                # Tu peux aussi afficher une alerte ici si besoin

            return HttpResponseRedirect(reverse("remerciement"))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form})


def remerciement_view(request):
    return HttpResponse("Merci de nous avoir contacté. Nous vous répondrons rapidement.")


def services_view(request):
    return render(request, 'services.html')

def a_propos_view(request):
    return render(request, 'a_propos.html')

