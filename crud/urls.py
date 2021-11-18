from django.urls import path
from . import views # un . representa el directorio/folder actual

urlpatterns = [
    #si dejalos las comillas vacias ('') es porque es nuestro Home Page, por dafult entra ahi
    path('', views.home, name='crud-home'),
    path('pedido/', views.pedido, name='crud-pedido'),
]
