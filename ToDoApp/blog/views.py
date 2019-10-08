


from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ArticlesModelform
# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Articles

class ArticlesCreateView(CreateView):
    template_name = 'articles/articles_create.html'
    form_class =  ArticlesModelform
    queryset = Articles.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticlesListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Articles.objects.all()

class ArticlesDetailView(DetailView):
    template_name = 'articles/articles_detail.html'
    queryset = Articles.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404 (Articles,id = id_)

class ArticlesUpdateView(UpdateView):
    template_name = 'articles/articles_create.html'
    form_class =  ArticlesModelform
    queryset = Articles.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404 (Articles,id = id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticlesDeleteView(DeleteView):
    template_name = 'articles/articles_delete.html'
    # queryset = Articles.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404 (Articles,id = id_)

    def get_success_url(self):
        return reverse ('articles:article-list')
