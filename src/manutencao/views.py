from django.shortcuts import render
from .models import Relatorio_Manutencao
from django.views.generic import ListView
from django.http import JsonResponse

# Create your views here.
class ManutencaoListView(ListView):
    model = Relatorio_Manutencao
    template_name = "manutencao/list.html"
    context_object_name = "relatorios"
    paginate_by = 20

    def get_queryset(self):
        order_by = self.request.GET.get('orderby', 'data_manutencao')
        return Relatorio_Manutencao.objects.all().order_by(order_by)
    
def relatorio_detail(request,id):
    relatorio = Relatorio_Manutencao.objects.get(id=id)
    data = {
        'data_manutencao': relatorio.data_manutencao.strftime('%d/%m/%Y'),
        'cidade': relatorio.cidade,
        'data_manutencao': relatorio.data_manutencao,
    }
    return JsonResponse(data)