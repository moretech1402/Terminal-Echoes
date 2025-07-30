from django.db import models

class Stat(models.Model):
    key = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name