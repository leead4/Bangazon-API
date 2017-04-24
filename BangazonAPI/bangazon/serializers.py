from BangazonAPI.bangazon.models import *
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Customer model to JSON
    Author: Jessica Younker

    """
    class Meta:
        """
        Global options for Customer class
        Author: Jessica Younker
        """
        model = Customer
        fields = ('firstname', 'lastname', 'status', 'date_created', 'date_last_active')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Convert ProductType model to JSON"""
    class Meta:
        """Global options for EmployeeTraining class"""
        model = ProductType
        fields = ('product_type', 'product_quantity')
