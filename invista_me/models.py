from django.db import models
from datetime import datetime

# Create your models here.

class Investimento(models.Model):
    # A partir daqui, criaremos todas as colunas que deverão ser armazenadas no banco de dados (seguiremos os itens (1) s (4) listados acima)
    investimento = models.TextField(max_length=255) # investimento é a primeira coluna da tabela, e apresenta tipo models.Textfield (campo texto). Dentro do parênteses do models.TextField tem muitas propriedades (estudar). Utilizamos só um, que é o comprimento total (255 linhas)
    valor = models.FloatField() # valor é a segunda coluna da tabela e apresenta tipo models.FloatField (valor decimal)
    pago = models.BooleanField(default=False) # identificará se foi pago ou não (verdadeiro ou falso). O valor padrão (inicial) é Falso
    data = models.DateField(default=datetime.now) 
