from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    quantidade = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.titulo, self.autor)

    