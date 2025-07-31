from rest_framework import serializers
from .models import Location, Cell, Stat, Character, CharacterStat, Monster, Shop, Chest

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class CharacterStatSerializer(serializers.ModelSerializer):
    stat_name = serializers.ReadOnlyField(source='stat.name')

    class Meta:
        model = CharacterStat
        fields = ['stat', 'value', 'stat_name']

class CharacterSerializer(serializers.ModelSerializer):
    character_stats = CharacterStatSerializer(source='stats', many=True, read_only=True)
    location_name = serializers.ReadOnlyField(source='current_cell.location.name')
    cell_coords = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = '__all__'

    def get_cell_coords(self, obj):
        if obj.current_cell:
            return f"({obj.current_cell.x_coord}, {obj.current_cell.y_coord})"
        return None

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class ChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chest
        fields = '__all__'

class CellSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Cell
        fields = ['id', 'location', 'x_coord', 'y_coord', 'cell_type', 'content_object']

    def get_content_object(self, obj):
        if obj.content_object:
            if isinstance(obj.content_object, Monster):
                return MonsterSerializer(obj.content_object).data
            elif isinstance(obj.content_object, Shop):
                return ShopSerializer(obj.content_object).data
            elif isinstance(obj.content_object, Chest):
                return ChestSerializer(obj.content_object).data
        return None