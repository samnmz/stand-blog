from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='detail'),
    path('list', views.ArticleListView.as_view(), name='list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search', views.search, name='search_article'),
    path('contactus', views.ContactUsView.as_view(), name='contactus'),
]
