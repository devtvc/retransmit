from django.shortcuts import render
from django.http import HttpResponse
from .models import Estacao, Relatorio_Manutencao
import json
from django.views.generic import ListView
from django.http import JsonResponse
from django.core.paginator import Paginator

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
   
    data = {
        'cidade': estacao.cidade,
        'uf': estacao.uf,
        'canal_virtual': estacao.canal_virtual,
        'potencia_projeto': estacao.potencia_projeto,
        'potencia_operacao': estacao.potencia_operacao,
        'responsabilidade_operacao': estacao.responsabilidade_operacao,
        'status_operacao': estacao.status_operacao,
        'status_telemetria': estacao.status_telemetria,

        # 'VISAO_GERAL': estacao.VISAO_GERAL.url,
    }
    return JsonResponse(data)

def disponibilidade_chart(request):
    estacoes = Estacao.objects.all()

    paginator = Paginator(estacoes, 10)  # Paginate results (25 stations per page)

    page_number = request.GET.get('page')  # Get the page number from the GET request
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object

    labels = []
    data = []

    # soma_disponibilidade = 0.0

    # for estacao in page_obj.object_list:
    #     relatorios = Relatorio_Manutencao.objects.filter(cidade=estacao.cidade)
    #     for relatorio in relatorios:
    #         soma_disponibilidade = soma_disponibilidade + relatorio.disponibilidade

    #     labels.append(estacao.cidade)

    #     if relatorios:
    #         disponibilidade_media = soma_disponibilidade / relatorios.count()
    #         data.append(disponibilidade_media)  # Use 0 if disponibilidade is None
    #     else:
    #         data.append(100)

    soma_diferenca = 0.0
    disponibilidade_media = 0.0

    for estacao in page_obj.object_list:
        relatorios = Relatorio_Manutencao.objects.filter(cidade=estacao.cidade)
        for relatorio in relatorios:
            soma_diferenca = soma_diferenca + relatorio.difference
            disponibilidade_media = round(100 - ((soma_diferenca / 30) * 100), 2)

        labels.append(estacao.cidade)

        if relatorios:
            data.append(disponibilidade_media)  # Use 0 if disponibilidade is None
        else:
            data.append(100)

    context = {
        'labels': json.dumps(labels),  # Ensure labels are valid JSON
        'data': json.dumps(data),      # Ensure data is valid JSON
        'page_obj': page_obj
    }

    return render(request, 'disponibilidade/chart.html', context)
    
