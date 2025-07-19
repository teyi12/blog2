from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Projet
from .forms import ProjetForm
from django.contrib.auth.decorators import login_required


from .forms import ArticleForm 
from .models import Article

def articles_view(request):
    articles = Article.objects.all().order_by ('-date_publication')
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/detail.html', context={'article': article})

def creer_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        form.save()
        return HttpResponseRedirect(reverse('articles:articles'))
    return render(request, 'articles/creer.html', context={'form':form})
   


def projets_liste(request):
    projets = Projet.objects.all().order_by('-date_creation')
    return render(request, 'projets/liste.html', {'projets': projets})

@login_required
def ajouter_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projets')
    else:
        form = ProjetForm()
    return render(request, 'projets/ajouter.html', {'form': form})


   

