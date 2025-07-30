from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Shop: {self.name}"

class Chest(models.Model):
    is_locked = models.BooleanField(default=True)
    gold_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Chest (Locked: {self.is_locked})"

class Monster(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Monster: {self.name}"
    