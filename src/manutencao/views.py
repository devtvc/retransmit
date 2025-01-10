from django.shortcuts import render
from .models import Relatorio_Manutencao
from django.views.generic import ListView
from django.http import JsonResponse

# Create your views here.
class ManutencaoListView(ListView):
    model = Relatorio_Manutencao
    template_name = "manutencao/list.html"
    context_object_name = "manutencoes"
    paginate_by = 20

    def get_queryset(self):
        order_by = self.request.GET.get('orderby', 'data_manutencao')
        return Relatorio_Manutencao.objects.all().order_by(order_by)
    
def manutencao_detail(request,id):
    manutencao = Relatorio_Manutencao.objects.get(id=id)
    data = {
        'data_reclamacao': manutencao.data_reclamacao.strftime('%d/%m/%Y'),
        'data_manutencao': manutencao.data_manutencao.strftime('%d/%m/%Y'),
        'cidade': manutencao.cidade,
        'uf': manutencao.uf,
        'autor_manutencao': manutencao.autor_manutencao,
        'tipo_manutencao': manutencao.tipo_manutencao,
        'comentario_manutencao': manutencao.comentario_manutencao,
        'pot_direta': manutencao.pot_direta,
        'pot_refletida': manutencao.pot_refletida,
        'exciter_power': manutencao.exciter_power,
        'nivel_CN': manutencao.nivel_CN,
        'nivel_recepcao': manutencao.nivel_recepcao,
        # 'VISAO_GERAL': manutencao.VISAO_GERAL.url,
    }
    return JsonResponse(data)
