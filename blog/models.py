from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    sinopsis = models.TextField()
    capitulos = models.IntegerField()
    estado = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/')
    video = models.FileField(upload_to='videos/')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre