"""gerenciador_tvcultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, sobre_page
from estacao.views import image_view, pdf_view, estacao_page, estacao_detail, EstacaoListView, disponibilidade_chart
from manutencao.views import ManutencaoListView, manutencao_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', estacao_page, name='home'),
    path('estacoes/', estacao_page, name='estacoes'),
    path('lista_estacoes/', EstacaoListView.as_view(), name='lista_estacoes'),
    path('lista_estacoes/<int:id>/', estacao_detail, name='estacao_detail'),
    path('disponibilidade/', disponibilidade_chart, name='disponibilidade'),
    path('manutencao/', ManutencaoListView.as_view(), name='manutencao'),
    path('manutencao/<int:id>/', manutencao_detail, name='manutencao_detail'),
    path('sobre/', sobre_page, name='sobre'),
    path('images/', image_view, name='image_view'),
    path('pdfs/', pdf_view, name='pdf_view'),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


