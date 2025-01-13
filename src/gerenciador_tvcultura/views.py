from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from estacao.models import Estacao

def home_page(request):
    station_count = Estacao.objects.count()
    context = {
        "title": "Sistema de gerência da rede do interior",
        "content": f"Número de Estações TV Cultura: { station_count }",
    }
    return render(request, 'home_page.html', context)

def sobre_page(request):
    context = {
        "title": "Sistema de gerência das estações retransmissoras TV Cultura",
        "content": "Engenharia & desenvolvimento de sistemas - FPA",
    }
    return render(request, 'sobre.html', context)