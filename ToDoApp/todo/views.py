from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from.models import Todoitem

# Create your views here.

def todoview(request):
    content_list = Todoitem.objects.all()

    # context = {
    #     'content_list:content_list'
    # }
    return render (request,'todo.html',{'all_items':content_list})


def addtodo(request):
    new_item = Todoitem(content = request.POST['content'])
    new_item.save()

    return HttpResponseRedirect ('/todo/')

def deletetodo(request,todo_id):
    delete_item = Todoitem.objects.get(id=todo_id)
    delete_item.delete()

    return HttpResponseRedirect ('/todo/')
