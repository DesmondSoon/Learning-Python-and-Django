from django.contrib import admin
from django.urls import path

from .views import (
    ArticlesListView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticlesListView.as_view(),name = 'article-list'),
]
