from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_ofx, name='upload_ofx'),
    path('transacoes/', views.listar_transacoes, name='listar_transacoes'),
    path('cliente/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/', views.listar_clientes, name='listar_clientes'),
    path('conta/nova/', views.cadastrar_conta, name='cadastrar_conta'),
    path('conta/', views.listar_contas, name='listar_contas'),
]