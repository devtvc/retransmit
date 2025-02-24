from django.db import models
from IBGE.models import Dados_IBGE

# Create your models here.
class Dados_Pagamento(models.Model):
    #cidade = models.CharField(max_length=100)
    #uf = models.CharField(max_length=10)
    def get_cidade_choices():
         # Fetch choices dynamically from the Cidade model
        unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
        return [(cidade, cidade) for cidade in unique_cidades]
    
    cidade = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
    )
    
    # def get_uf_choices():
    #      # Fetch choices dynamically from the Cidade model
    #     unique_ufs = Dados_IBGE.objects.values_list('uf', flat=True).distinct()
    #     return [(uf, uf) for uf in unique_ufs]
    
    # uf = models.CharField(
    #     max_length=100,
    #     choices=get_uf_choices,
    #     blank=True,
    #     null=True,
    # )
    UFs = [
        ('item1', 'SP'),
        ('item2', 'DF'),
    ]
    uf = models.CharField(max_length=10, choices=UFs, default='item1')


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
    ]

    tipo_conta = models.CharField(max_length=100, choices=TIPO_CONTA, default='item1')
    

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
    )
    conta_paga_a = models.CharField(max_length=100, help_text="Digite o CNPJ ou CPF")
    razao_social_receptor = models.CharField(max_length=100, default="", help_text="Digite a razão social do CPF/CNPJ informado acima")
    valor_bruto_conta = models.FloatField(null=True, blank=True, help_text="Digite o valor bruto da conta em R$")
    valor_liquido_conta = models.FloatField(null=True, blank=True, help_text="Digite o valor líquido da conta em R$")
    conta_digitalizada = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Conta digitalizada (PDF)")
    comentarios = models.TextField(null=True, blank=True, help_text="Escreva outras observações da conta. Ex.: Número de contrato, consumo no mês etc")
   
    class Meta:
        ordering = ['-mes_referencia']
        db_table = "rede_dados_pagamento"
        verbose_name = "Dados Pagamentos"  # Singular name
        verbose_name_plural = "Dados Pagamentos"  # Plural name

    def __str__(self):
        
        return f"{self.cidade}"