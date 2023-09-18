from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('sidebar', views.render_sidebar, name='render_sidebar'),
]
