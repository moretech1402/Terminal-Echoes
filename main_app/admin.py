# type: ignore

from django.contrib import admin
from .models import *

class CharacterStatInline(admin.TabularInline):
    model = CharacterStat
    extra = 1

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name')
    search_fields = ('name', 'owner_name')

@admin.register(Chest)
class ChestAdmin(admin.ModelAdmin):
    list_display = ('is_locked', 'gold_amount')

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ('location', 'x_coord', 'y_coord', 'cell_type', 'content_object')
    list_filter = ('location', 'cell_type')
    search_fields = ('description',)
    fields = ('location', 'x_coord', 'y_coord', 'cell_type', 'description', 'content_type', 'object_id')

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('name', 'key')
    search_fields = ('name', 'key')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'current_cell')
    list_filter = ('user', 'current_cell__location')
    inlines = [CharacterStatInline]