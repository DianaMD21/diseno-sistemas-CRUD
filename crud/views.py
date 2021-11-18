from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'crud/home.html')

def about(request):
    return render(request,'crud/pedido.html', {'title': 'Pedido'})