from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def feriados(request):
    hoje = date.today()
    feriado = FeriadoModel.objects.filter(data=hoje).first()

    if feriado:
        return render(request, 'feriados.html', {'feriado' : feriado})
    else:
        return render(request, 'nao_e_feriado.html')

