from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from main import models
from .form import ArticleForm, LoginForm, RegisterForm
# Create your views here.

def index(request):
    latest_articles = models.Article.objects.all().order_by('-created_at')[:10]
    return render(request, 'main/index.html', {'latest_articles' : latest_articles})

def article(request, pk):
    article = get_object_or_404(models.Article, pk = pk)
    return render(request, 'main/article.html', {'article' : article})

def author(request, pk):
    author = get_object_or_404(User , pk = pk)
    return render(request, 'main/author.html', {'author' : author})

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit = False)
            article.author = User.objects.get(username = request.user.username)
            article.save()
            return redirect('article', pk = article.pk)
    else:
        form = ArticleForm()
        return render(request, 'main/create_article.html', {'form' : form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                django_login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Invalid Credientials', status=401 )
    else:
        form = LoginForm()
        return render(request, 'main/login.html', {'form' : form})


def logout(request):
    django_logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            django_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
        return render(request, 'main/register.html', {'form' : form})

