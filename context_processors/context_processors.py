from blog.models import Article, Category


def recent_article(request):
    recent_articles = Article.objects.order_by('-updated')
    category = Category.objects.all()
    return {'recent_articles': recent_articles, 'category': category}
