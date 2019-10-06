from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import players
from .forms import playersform
# Create your views here.


# def deletetodo(request,todo_id):
#     delete_item = Todoitem.objects.get(id=todo_id)
#     delete_item.delete()
#
#     return HttpResponseRedirect ('/players/')
#

# def player_delete_redirect (request):
#     return redirect (reverse('url-for-player_delete.html'))

def player_delete (request,player_id):

    delete_player = players.objects.get(id=player_id)

    if request.method == 'POST':
        delete_player.delete()
        return redirect ('players')
    context = {
        "object": delete_player
    }

    return render (request,'player_delete.html', context)

# def player_delete (request,player_id):
#
#     obj = get_object_or_404 (players, id = player_id)
#
#     if request.method == 'POST':
#         obj.delete()
#         return redirect ("../")
#
#     context = {
#         "object":obj
#     }
#
#     return render (request,'player_delete.html', context)

def dynamic_player_view (request, player_id):
    # try:
    #     obj = players.objects.get(id=player_id)
    # except Product.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404 (players, id = player_id)

    context = {
        'object':obj,
    }
    return render (request,'player_detail.html',context)




def player_info (request):
    queryset = players.objects.all()

    context = {
        'player_list':queryset,
    }

    return render (request,'playerview.html',context)

def player_create_info (request):
    # player_data = players.objects.all()
    form = playersform(request.POST or None)
    if form.is_valid():
        form.save()
        form = playersform()
    context = {
        'form':form,
    }

    return render (request,'player_create.html',context)

# def player_delete_info (request):
