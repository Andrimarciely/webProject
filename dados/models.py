from django.db import models

class Parametro(models.Model):
    descricao_parametro=models.CharField(max_length=100, help_text='nome do agente químico')
    unidade_de_medida_do_parametro=models.CharField(max_length=10, help_text='unidade de medida do agente químico')
    resultado=models.CharField(max_length=10, help_text='valor mensurado do agente químico na amostra')
    lq=models.CharField(max_length=100, help_text='valor de referência')

    def __str__(self):
        return self.descricao_parametro


class Amostra(models.Model):
    codigo_interno=models.CharField(max_length=50, help_text='Código de identificação interna ACME')
    setor_local_avaliado=models.CharField(max_length=100, help_text='')
    hora_da_coleta=models.CharField(max_length=100, help_text='')
    data_da_coleta=models.DateField()
    metodo_de_analise=models.CharField(max_length=100, help_text='')
    descricao_do_metodo=models.CharField(max_length=100, help_text='')
    data_de_entrada_no_laboratorio=models.DateField()
    data_do_relatorio_de_ensaio=models.DateField()
    unidade_de_medida=models.CharField(max_length=100, help_text='')
    volume=models.CharField(max_length=10, help_text='')
    conclusao=models.CharField(max_length=200, help_text='')
    observacao=models.CharField(max_length=200, help_text='')
    irregularidades=models.CharField(max_length=200, help_text='')
    parametro=models.ForeignKey(Parametro, on_delete=models.CASCADE)


    def __str__(self):
        return self.codigo_interno
class Formulario_de_Amostra(models.Model):
    id_solicitacao_de_serviço=models.CharField(max_length=200, help_text='')
    tipo_de_amostra=models.CharField(max_length=200, help_text='')
    data_de_coleta=models.DateField()
    amostra=models.ForeignKey(Parametro, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_de_amostra

class Solicitacao_de_Serviço(models.Model):

    nome_cliente=models.CharField(max_length=200, help_text='')
    empresa_avaliada=models.CharField(max_length=200, help_text='')
    lugar_de_coleta=models.CharField(max_length=200, help_text='')
    formulario_de_amostra = models.ForeignKey(Parametro, on_delete=models.CASCADE)