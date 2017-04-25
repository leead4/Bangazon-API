from BangazonAPI.models import *
from rest_framework import viewsets
from BangazonAPI.serializers import *
from BangazonAPI.models import *




class ProductTypeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows customers to be viewed or edited."""
    queryset = ProductType.objects.all()
    serializer_class  = ProductTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """API endpoint that allows customers to be viewed or edited."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    Author: Jessica Younker
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PaymentTypes to be viewed or edited.
    """
    queryset = PaymentType.objects.all().order_by("payment_type_provider")
    serializer_class = PaymentTypeSerializer

    


