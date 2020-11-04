from rest_framework import viewsets
from .models import Prestasi
from .serializers import PrestasiSerializer

class PrestasiViewSet(viewsets.ModelViewSet):
    queryset = Prestasi.objects.all()
    serializer_class = PrestasiSerializer