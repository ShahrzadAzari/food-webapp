from django.shortcuts import render, redirect
from .models import Foods
# Create your views here.

def first(request):
    if request.method == 'GET' :
        return render(request, 'home.html')

def all(request):
    if request.method == 'GET' :
        return render(request, 'citysearch.html')

def addfood(request):
    if request.method == 'GET' :
        return render(request, 'addfood.html')
    elif request.method == 'POST' :
        name = request.POST.get('name')
        city = request.POST.get('city')
        time = request.POST.get('time')
        material = request.POST.get('material')
        how = request.POST.get('how')
        points = request.POST.get('points')
        new = Foods.objects.create(name=name, city=city, time=time, material=material, how=how, points=points)
        return redirect('/addfood')

def search(request):
    v= request.GET.get('city')
    t= Foods.objects.filter(city=v)    
    return render(request, 'city.html', context={'h':t})
     
def detail(request):
    id = request.GET.get('id')
    t = Foods.objects.get(id=int(id))
    return render(request, 'detail.html', status=200, context={'y': t})