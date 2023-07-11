from rest_framework.serializers import ModelSerializer
from .models import Contacto

class ContactoSerializer(ModelSerializer):
    class Meta:
        model = Contacto
        fields = "__all__"