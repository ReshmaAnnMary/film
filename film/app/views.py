from django.shortcuts import render, redirect
from .forms import Form
from .models import Movies


# Create your views here.


def index(request):
    movie = Movies.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def details(request, id):
    value = Movies.objects.get(id=id)
    return render(request, 'details.html', {'value': value})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        data = Movies(name=name, desc=desc, year=year, img=img)
        data.save()
    return render(request, 'add.html')


def update(request, id):
    value = Movies.objects.get(id=id)
    form = Form(request.POST or None, request.FILES, instance=value)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': value})


def delete(request, id):
    if request.method == 'POST':
        id = Movies.objects.get(id=id)
        id.delete()
        return redirect('/')
    return render(request, 'delete.html')