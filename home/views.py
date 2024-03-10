from django.shortcuts import render
from blog.models import Article, Category


def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/home.html', {'articles': articles, 'categories': categories})
