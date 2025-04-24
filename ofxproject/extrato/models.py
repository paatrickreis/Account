from django.db import models

class Conta(models.Model):
    TIPOS = [
        ('CC', 'Conta Corrente'),
        ('CP', 'Conta Poupança'),
    ]
    tipo = models.CharField(max_length=2, choices=TIPOS)
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.banco} - {self.agencia}/{self.numero}"

class Extrato(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='extratos')
    mes = models.IntegerField()
    ano = models.IntegerField()
    arquivo = models.FileField(upload_to='extratos/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Extrato {self.mes}/{self.ano} - {self.conta}"

class Transacao(models.Model):
    extrato = models.ForeignKey(Extrato, on_delete=models.CASCADE, related_name='transacoes')
    data = models.DateField()
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} - {self.descricao} - R$ {self.valor}"

class Transacao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} - {self.descricao} - R$ {self.valor}"