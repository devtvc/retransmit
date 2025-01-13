from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacao
from .models import Relatorio_Manutencao
import json
from django.views.generic import ListView
from django.http import JsonResponse

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


class EstacaoListView(ListView):
    model = Estacao
    template_name = "estacao/list.html"
    context_object_name = "estacoes"
    paginate_by = 300

    def get_queryset(self):
        order_by = self.request.GET.get('orderby', 'cidade')
        return Estacao.objects.all().order_by(order_by)
    
def estacao_detail(request,id):
    estacao = Estacao.objects.get(id=id)
    manutencao = Relatorio_Manutencao.objects.filter(cidade=estacao.cidade).first()
    disponibilidade = manutencao.disponibilidade if manutencao else 100
    data = {
        'cidade': estacao.cidade,
        'uf': estacao.uf,
        'canal_virtual': estacao.canal_virtual,
        'potencia_projeto': estacao.potencia_projeto,
        'potencia_operacao': estacao.potencia_operacao,
        'responsabilidade_operacao': estacao.responsabilidade_operacao,
        'status_operacao': estacao.status_operacao,
        'status_telemetria': estacao.status_telemetria,
        'disponibilidade': disponibilidade,

        # 'VISAO_GERAL': estacao.VISAO_GERAL.url,
    }
    return JsonResponse(data)
