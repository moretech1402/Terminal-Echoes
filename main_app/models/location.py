from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
        

class CellType(models.TextChoices):
    EMPTY = 'EM', 'Empty'
    WALL = 'WL', 'Wall'
    WATER = 'WT', 'Water'
    SHOP = 'SH', 'Shop'
    QUEST = 'QG', 'Quest Giver'

class Cell(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
    
    cell_type = models.CharField(
        max_length=2,
        choices=CellType.choices,
        default=CellType.EMPTY,
    )
    description = models.TextField(blank=True, null=True)

    # --- Generic Foreign Key ---
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('location', 'x_coord', 'y_coord')

    def __str__(self) -> str:
        content_info = f" ({self.content_object})" if self.content_object else ""
        return f"Cell ({self.x_coord}, {self.y_coord}) in {self.location.name}{content_info}"