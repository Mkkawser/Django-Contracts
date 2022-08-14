from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Contract


def home(request):
    if 'q' in request.GET:
        q = request.GET.get('q')  #search
        post = Contract.objects.filter(name__icontains=q)
        dic = {
            'data': post
        }
    else:
        dic = {
            'data': Contract.objects.all().order_by('name').values(),
        }
    return render(request, 'index.html', dic)


def add_cont(request):
    if request.method == 'POST':
        user = Contract()
        user.name = request.POST.get('name')
        user.number = request.POST.get('number')
        if len(user.name) > 0:
            user.save()
        return redirect('/')
    return render(request, 'index.html')


def del_cont(request, val):
    p = Contract.objects.get(pk=val).delete()
    return redirect('home')


def edit_cont(request, val):
    if request.method == 'POST':
        user = Contract.objects.get(pk=val)  #get current id
        user.name = request.POST.get('name')
        user.number = request.POST.get('number')
        user.save()    #save
        return redirect('/')
    dic = {
        'data': Contract.objects.get(pk=val)
    }
    return render(request, 'edit.html', dic)
