from django.db import models
from django.utils import timezone
from django.db.models import Count
from django.utils.timezone import now
from django.core.exceptions import ValidationError


# Create your models here.
class Relatorio_Manutencao(models.Model):
    def get_cidade_choices():
        from IBGE.models import Dados_IBGE
         # Fetch choices dynamically from the Cidade model
        unique_cidades = Dados_IBGE.objects.values_list('cidade', flat=True).distinct()
        return [(cidade, cidade) for cidade in unique_cidades]
    
    cidade = models.CharField(
        max_length=100,
        choices=get_cidade_choices,
        blank=True,
        null=True,
    )
    id = models.AutoField(primary_key=True)
    #cidade = models.CharField(max_length=100)

    # def get_uf_choices():
    #     from IBGE.models import Dados_IBGE
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

    data_reclamacao = models.DateTimeField(null=True, blank=True)
    data_manutencao = models.DateTimeField(null=True, blank=True)

    def clean(self):
        super().clean()

        current_time = now()

        # Garante que os dois campos tem um valor
        if self.data_reclamacao and self.data_manutencao:
            # Garante que a data de manutenção seja maior que a data de reclamação
            if self.data_manutencao <= self.data_reclamacao:
                raise ValidationError({
                    'data_manutencao': "A Data de Manutenção deve ser maior que a Data de Reclamação."
                })

            # Checa se a diferença entre as datas de reclamação e manutenção é menor que 30 dias
            delta_days = (self.data_manutencao - self.data_reclamacao).days
            if delta_days > 30:
                raise ValidationError({
                    'data_manutencao': "A diferença entre Data de Manutenção e Data de Reclamação não pode ser maior que 30 dias."
                })

            # Garante que as duas datas são menores que a data atual
            if self.data_reclamacao > current_time:
                raise ValidationError({
                    'data_reclamacao': "A Data de Reclamação deve ser anterior à data atual."
                })

            if self.data_manutencao > current_time:
                raise ValidationError({
                    'data_manutencao': "A Data de Manutenção deve ser anterior à data atual."
                })
       
    
    # disponibilidade = models.FloatField(null=True, blank=True, editable=False)

    difference = models.FloatField(null=True, blank=True, editable=False)

    # def save(self, *args, **kwargs):
    #     if self.data_reclamacao and self.data_manutencao:
    #         difference = (self.data_manutencao - self.data_reclamacao).days
    #         self.disponibilidade = round(100 - ((difference / 30) * 100), 2)
    #     else:
    #         # Set disponibilidade to 100 if either date is missing
    #         self.disponibilidade = 100.0
    #     super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.data_reclamacao and self.data_manutencao:
            self.difference = (self.data_manutencao - self.data_reclamacao).days
        else:
            # Set diferenca para 0 se não há dados
            self.difference = 0
        super().save(*args, **kwargs)

    TECNICO_MANUT = [
        ('item1', 'ARI LIMA'),
        ('item2', 'RODRIGO AGUADO'),
        ('item3', 'PEDRO'),
        ('item4', 'TANIS'),
        ('item5', 'ALEXANDRE COSME'),
        ('item6', 'ELIAS'),
    ]

    tecnico_manutencao = models.CharField(max_length=50, choices=TECNICO_MANUT, default='item1')
    TIPO_MANUT = [
        ('item1', 'PREVENTIVA'),
        ('item2', 'CORRETIVA'),
        ('item3', 'EMERGENCIAL'),
    ]
    
    tipo_manutencao = models.CharField(max_length=10, choices=TIPO_MANUT, default='item1')
    comentario_manutencao = models.TextField(blank=True)
    pot_direta = models.FloatField(null=True, blank=True, help_text="Leitura da potência direta em W")
    pot_refletida = models.CharField(max_length=10, blank=True, help_text="Leitura da potência direta em W")
    exciter_power = models.FloatField(null=True, blank=True, help_text="Leitura do nível de excitação em dBm")
    nivel_CN = models.FloatField(null=True, blank=True, help_text="Leitura de C/N em dB")
    nivel_recepcao = models.FloatField(null=True, blank=True, help_text="Leitura do nível de recepção em dBm")
    VISTA_FRONTAL_TX = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    VISTA_TRASEIRA_TX = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ANTENA_DE_RECEPCAO = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ANTENA_DE_TRANSMISSAO_E_DA_TORRE = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ABRIGO_1_INTERNO = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ABRIGO_2_INTERNO = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ABRIGO_1_EXTERNO = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    ABRIGO_2_EXTERNO = models.ImageField(upload_to='manutencao/', blank=True, null=True)
    VISAO_GERAL = models.ImageField(upload_to='manutencao/', blank=True, null=True)

    class Meta:
        ordering = ['cidade']
        db_table = 'rede_relatorio_manutencao'
        verbose_name = "Relatório Manutenção"  # Singular name
        verbose_name_plural = "Relatório Manutenção"  # Plural name


    def __str__(self):
        data_manutencao_local = timezone.localtime(self.data_manutencao) if self.data_manutencao else None
        return f"{self.cidade} - {data_manutencao_local}"
    