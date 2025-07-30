from django.db import models
from django.conf import settings

from .location import Cell

class Stat(models.Model):
    key = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_cell = models.ForeignKey(Cell, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name} (User: {self.user.username})"
