from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[0:3]
    return render(request, 'home.html',
                  {'articles': articles, 'recent_articles': recent_articles})


def render_sidebar(request):
    return render(request, 'includes/sidebar.html', {})
