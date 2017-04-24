from BangazonAPI.bangazon.models import *
from rest_framework import viewsets
from BangazonAPI.bangazon.serializers import *


class CustomerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows customers to be viewed or edited."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint that allows products to be viewed or edited."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
