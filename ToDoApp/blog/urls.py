from django.contrib import admin
from django.urls import path

from .views import (
    ArticlesDetailView,
    ArticlesListView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticlesListView.as_view(),name = 'article-list'),
    path('<int:pk>/',ArticlesDetailView.as_view(),name= 'article-detail')
]
