from django.db import models
from django.urls import reverse

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    class Meta:
        ordering = ['-precio']  # 🔹 Ordena por precio
        
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('productos:detalle', args=[self.pk])
