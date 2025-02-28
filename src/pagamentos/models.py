from django.db import models
from IBGE.models import Dados_IBGE
from django.db.models import Sum

# Create your models here.
class Dados_Pagamento(models.Model):
    
    def get_cidade_choices():
        
        unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
        return [(cidade, cidade) for cidade in unique_cidades]
    
    cidade = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
    )
    
    UFs = [
        ('item1', 'SP'),
        ('item2', 'DF'),
    ]
    uf = models.CharField(max_length=10, choices=UFs, default='item1', verbose_name="UF")


    PAGO_POR = [
        ('item1', 'FPA'),
        ('item2', 'PM'),
        ('item3', 'PMSP'),
    ]
    TIPO_CONTA = [
        ('item1', 'ÁGUA'),
        ('item2', 'ENERGIA'),
        ('item3', 'ALUGUEL'),
        ('item4', 'IPTU'),
        ('item5', 'TELEFONE'),
        ('item6', 'MÃO DE OBRA'),
        ('item7', 'SERVIÇOS EVENTUAIS'),
        ('item8', 'CONTRATOS'),
        ('item9', 'CRÉDITO ROTATIVO (CAIXINHA)'),
        ('item10', 'OUTROS - DETALHAR EM COMENTÁRIOS'),
    ]

    tipo_conta = models.CharField(max_length=100, choices=TIPO_CONTA, default='item1', verbose_name="Tipo da conta")
    

    MESES = [
        ('01', 'Janeiro'),
        ('02', 'Fevereiro'),
        ('03', 'Março'),
        ('04', 'Abril'),
        ('05', 'Maio'),
        ('06', 'Junho'),
        ('07', 'Julho'),
        ('08', 'Agosto'),
        ('09', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    ]
    mes_referencia = models.CharField(
        max_length=2,
        choices=MESES,
        blank=True,  
        null=True,
        verbose_name="Mês de referência" 
    )
    conta_paga_a = models.CharField(max_length=100, help_text="Digite o CNPJ ou CPF", verbose_name="Conta paga à (CNPJ):")
    razao_social_receptor = models.CharField(max_length=100, default="", help_text="Digite a razão social do CPF/CNPJ informado acima", verbose_name="Razão social do receptor")
    valor_bruto_conta = models.FloatField(null=True, blank=True, help_text="Digite o valor bruto da conta em R$", verbose_name="Valor bruto da conta")
    valor_liquido_conta = models.FloatField(null=True, blank=True, help_text="Digite o valor líquido da conta em R$", verbose_name="Valor líquido da conta")
    conta_digitalizada = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Conta digitalizada (PDF)")
    comentarios = models.TextField(null=True, blank=True, help_text="Escreva outras observações da conta. Ex.: Número de contrato, consumo no mês etc", verbose_name="Comentários")
   
    class Meta:
        ordering = ['-mes_referencia']
        db_table = "rede_dados_pagamento"
        verbose_name = "Dados Pagamentos"  # Singular name
        verbose_name_plural = "Dados Pagamentos"  # Plural name

    def __str__(self):
        return f"{self.cidade}"