from django.contrib import admin
from .models import Cliente, Conta, Extrato, Transacao

admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Extrato)
admin.site.register(Transacao)
