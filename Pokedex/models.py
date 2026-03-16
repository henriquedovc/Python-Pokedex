# Pokedex/models.py

from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Pokemon(models.Model):
    numero          = models.IntegerField(unique=True)
    nome            = models.CharField(max_length=100)
    descricao       = models.TextField(blank=True)
    foto_url        = models.URLField(max_length=500)
    foto_shiny      = models.URLField(max_length=500, blank=True)
    altura          = models.FloatField()
    peso            = models.FloatField()
    tipos           = models.ManyToManyField(Tipo, related_name='pokemons')
    hp              = models.IntegerField()
    ataque          = models.IntegerField()
    defesa          = models.IntegerField()
    ataque_especial = models.IntegerField()
    defesa_especial = models.IntegerField()
    velocidade      = models.IntegerField()

    def __str__(self):
        return f'#{self.numero:03d} {self.nome}'

    class Meta:
        verbose_name = 'Pokémon'
        verbose_name_plural = 'Pokémons'
        ordering = ['numero']