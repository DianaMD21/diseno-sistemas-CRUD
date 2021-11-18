from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'crud/home.html')
    #return HttpResponse('<h1>HOME</h1>')

def pedido(request):
    return render(request,'crud/pedido.html', {'title': 'Pedido'})