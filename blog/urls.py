from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/edit/<int:id>/', views.article_edit, name='article_edit'),
]
