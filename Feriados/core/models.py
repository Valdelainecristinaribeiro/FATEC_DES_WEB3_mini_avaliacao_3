from django.db import models

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=70)
    data = models.DateField()

    def __str__(self):
        return self.nome