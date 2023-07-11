from rest_framework.viewsets import ModelViewSet
from .models import Contacto
from .serializers import ContactoSerializer

class ContactoViewSet(ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer