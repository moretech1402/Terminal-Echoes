from rest_framework import viewsets
from .models import Location, Cell, Stat, Character, CharacterStat
from .serializers import (
    LocationSerializer,
    CellSerializer,
    StatSerializer,
    CharacterSerializer,
    CharacterStatSerializer,
)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterStatViewSet(viewsets.ModelViewSet):
    queryset = CharacterStat.objects.all()
    serializer_class = CharacterStatSerializer