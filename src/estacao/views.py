from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacao
import json

# Create your views here.
def estacao_page(request):
    station_count = Estacao.objects.count()
    context = {
        "title": "Sistema de gerência da rede do interior",
        "content": f"Número de Estações TV Cultura: { station_count }",
    }
    estacoes = ['TV Cultura', 'TV Cultura Paulista', 'TV Cultura Brasília']
    valores = [10, 20, 30]
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
