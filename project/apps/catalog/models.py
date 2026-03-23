from django.db import models
from apps.users.models import customuser as user
# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='catalog/imagenes/', null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
class topics_group(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default="unknown")
    users_joined = models.ManyToManyField(user,blank=True)
    
    imagen = models.ImageField(upload_to='', null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)
    posts = models.ManyToManyField('post', blank=True)
    def __str__(self):
        return self.nombre

class topic_section(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(topics_group, on_delete=models.CASCADE, related_name='sections')

class post(models.Model):
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('topics_group', on_delete=models.CASCADE, related_name='post', null=True)