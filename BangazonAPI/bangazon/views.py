from BangazonAPI.bangazon.models import Customer
from rest_framework import viewsets
from BangazonAPI.bangazon.serializers import *


class CustomerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows customers to be viewed or edited."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
