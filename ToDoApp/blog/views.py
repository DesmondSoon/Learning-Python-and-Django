from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Articles


class ArticlesListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Articles.objects.all()

class ArticlesDetailView(DetailView):
    template_name = 'articles/articles_detail.html'
    queryset = Articles.objects.all()
