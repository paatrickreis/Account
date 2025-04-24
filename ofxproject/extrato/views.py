from django.shortcuts import render, redirect
from .forms import UploadOFXForm, ClienteForm, ContaForm
from ofxparse import OfxParser
from .models import Transacao, Extrato, Cliente, Conta
import io


def upload_ofx(request):
    if request.method == 'POST':
        form = UploadOFXForm(request.POST, request.FILES)
        if form.is_valid():
            conta = form.cleaned_data['conta']
            mes = form.cleaned_data['mes']
            ano = form.cleaned_data['ano']
            arquivo = form.cleaned_data['arquivo']

            extrato = Extrato.objects.create(conta=conta, mes=mes, ano=ano, arquivo=arquivo)

            arquivo_ofx = arquivo.read().decode('utf-8')
            ofx = OfxParser.parse(io.StringIO(arquivo_ofx))
            conta_ofx = ofx.account
            for t in conta_ofx.statement.transactions:
                Transacao.objects.create(
                    extrato=extrato,
                    data=t.date,
                    descricao=t.payee,
                    valor=t.amount
                )
            return redirect('listar_transacoes')
    else:
        form = UploadOFXForm()

    return render(request, 'extrato/upload.html', {'form': form})


def listar_transacoes(request):
    transacoes = Transacao.objects.select_related('extrato__conta').all().order_by('-data')
    return render(request, 'extrato/lista.html', {'transacoes': transacoes})


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'extrato/cliente_form.html', {'form': form})


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'extrato/cliente_lista.html', {'clientes': clientes})


def cadastrar_conta(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contas')
    else:
        form = ContaForm()
    return render(request, 'extrato/conta_form.html', {'form': form})


def listar_contas(request):
    contas = Conta.objects.select_related('cliente').all()
    return render(request, 'extrato/conta_lista.html', {'contas': contas})
