from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'skynet/index.html')
def hunt(request, id):
    data = {"id": id, "message": "Don't go to the python", "acces": "1"}
    return render(request, 'skynet/hunt.html', context=data)

def blog(request):
    return render(request, 'skynet/blog.html')

def home(request):
    return render(request, 'skynet/home.html')

def about(request):
    return render(request, 'skynet/about.html')

def unigodoo(request):
    return render(request, 'skynet/unigodoo.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Вам в Рай</h1>')
# Create your views here.
