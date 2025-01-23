from django.db import models


class Processos_Anatel(models.Model):
    cidade = models.CharField(max_length=100, default="")
    uf = models.CharField(max_length=10, default="")
    local_especifico = models.CharField(max_length=100, blank=True, null=True, verbose_name="Local específico da estação")
    prazo_anatel = models.DateField(null=True, blank=True, verbose_name="Prazo limite junto à Anatel/MCOM")
    ACOES = [
        ('item1', 'ENTRAR EM OPERAÇÃO'),
        ('item2', 'PAGAR PPDUR'),
        ('item3', 'LICENCIAR'),
        ('item4', 'OUTROS'),
    ]
    acao = models.CharField(max_length=100, choices=ACOES, blank=True, default="item1", verbose_name="Ação")
    relatorio_conformidade = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Relatório de conformidade")
    laudo_vistoria = models.FileField(upload_to='pdfs/', blank=True, null=True, verbose_name="Laudo de vistoria")
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-prazo_anatel']
        db_table = 'rede_processos_anatel'
        verbose_name = "Processos Anatel"  # Singular name
        verbose_name_plural = "Processos Anatel"  # Plural name


    def __str__(self):
        return self.cidade