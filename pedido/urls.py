from django.urls import path
from . import views
from .views import efetuar_pedido

urlpatterns = [
    path("finalizar_pedido/", views.finalizar_pedido, name='finalizar_pedido'),
    path("validaCupom/", views.validaCupom, name='validaCupom'),
    path('efetuar_pedido/', efetuar_pedido, name='efetuar_pedido'),

]
