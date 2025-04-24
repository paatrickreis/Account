from django.shortcuts import render, redirect
from .forms import UploadOFXForm
from ofxparse import OfxParser
from .models import Transacao
import io

def upload_ofx(request):
    if request.method == 'POST':
        form = UploadOFXForm(request.POST, request.FILES)
        if form.is_valid():
            ofx_file = request.FILES['arquivo']
            ofx = OfxParser.parse(io.TextIOWrapper(ofx_file, encoding='utf-8'))
            conta = ofx.account
            for t in conta.statement.transactions:
                Transacao.objects.create(
                    data=t.date,
                    descricao=t.payee,
                    valor=t.amount
                )
            return redirect('listar_transacoes')
    else:
        form = UploadOFXForm()

    return render(request, 'extrato/upload.html', {'form': form})

def listar_transacoes(request):
    transacoes = Transacao.objects.all().order_by('-data')
    return render(request, 'extrato/lista.html', {'transacoes': transacoes})