from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def estacao_page(request):
    # station_count = Estacao.objects.count()
    estacoes = ['TV Cultura', 'TV Cultura Paulista', 'TV Cultura Brasília']
    valores = [10, 20, 30]
    return render(request, 'estacoes.html', {
        'station_count': len(estacoes),
        'estacoes': json.dumps(estacoes),
        'valores': json.dumps(valores),
        })

def image_view(request):
    # Your logic to serve an image or list images here
    return HttpResponse("This is a custom image view.")

def pdf_view(request):
    # Your logic to serve an pdf file here
    return HttpResponse("This is a custom pdf view.")
