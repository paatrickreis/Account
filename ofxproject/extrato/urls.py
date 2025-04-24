from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_ofx, name='upload_ofx'),
    path('transacoes/', views.listar_transacoes, name='listar_transacoes'),
]
