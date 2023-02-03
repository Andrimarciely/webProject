from django.contrib import admin
from .models import Parametro, Amostra, Formulario_de_Amostra, Solicitacao_de_Servico,Lista_de_Servico
# Register your models here.
admin.site.register(Parametro)
admin.site.register(Amostra)
admin.site.register(Formulario_de_Amostra)
admin.site.register(Solicitacao_de_Servico)
admin.site.register(Lista_de_Servico)