from django.shortcuts import render, redirect
from .models import movie
from .forms import Movie

# Create your views here.
def index(request):
    film = movie.objects.all()
    context = {
        'list' : film
    }
    return render(request,'index.html',context)

def details(request,id):
    film = movie.objects.get(id=id)
    return render(request,'details.html',{'movie':film})
def add_movie(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        film = movie(name=name,desc=desc,year=year,img=img)
        film.save()

    return render(request,'add.html')

def edit(request,id):
    film = movie.objects.get(id=id)
    form = Movie(request.POST or None, request.FILES,instance=film)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':film})

def delete(requset,id):
    if requset.method == 'POST':
        film = movie.objects.get(id=id)
        film.delete()
        return redirect('/')
    return render(requset,'delete.html')