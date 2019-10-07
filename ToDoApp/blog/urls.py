from django.contrib import admin
from django.urls import path

from .views import (
    ArticlesDetailView,
    ArticlesCreateView,
    ArticlesListView,
    ArticlesUpdateView,

)

app_name = 'articles'
urlpatterns = [
    path('', ArticlesListView.as_view(),name = 'article-list'),
    path('<int:id>/',ArticlesDetailView.as_view(),name= 'article-detail'),
    path('create/',ArticlesCreateView.as_view(),name= 'article-create'),
    path('<int:id>/update/',ArticlesUpdateView.as_view(),name= 'article-update')
]
