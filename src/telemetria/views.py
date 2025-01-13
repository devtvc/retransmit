from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacao
import json

# Create your views here.
def estacao_page(request):
    station_count = Estacao.objects.count()
    station_tvc_count = Estacao.objects.filter(responsabilidade_operacao='TV CULTURA').count()
    station_tvcp_count = Estacao.objects.filter(responsabilidade_operacao='TVC PAULISTA').count()
    station_tvcb_count = Estacao.objects.filter(responsabilidade_operacao='TVC BRASÍLIA').count()
    station_tvcn_count = Estacao.objects.filter(responsabilidade_operacao='TV COSTA NORTE').count()
    context = {
        "title": "Operação das estações retransmissoras",
        "content": f"Número total de estações: { station_count }",
    }
    estacoes = ['TV Cultura', 'TVC Paulista', 'TVC Brasília', 'TV COSTA NORTE']
    valores = [station_tvc_count, station_tvcp_count, station_tvcb_count, station_tvcn_count]
    context.update({        
        'estacoes': json.dumps(estacoes),
        'valores': json.dumps(valores),})
    
    return render(request, 'estacoes.html', context)

def image_view(request):
    # Your logic to serve an image or list images here
    return HttpResponse("This is a custom image view.")

def pdf_view(request):
    # Your logic to serve an pdf file here
    return HttpResponse("This is a custom pdf view.")
