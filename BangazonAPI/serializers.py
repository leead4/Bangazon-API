from BangazonAPI.models import *
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
        fields = ('firstname', 'lastname', 'status', 'date_created','date_last_active')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Convert Product model to formatted JSON string listing."""

    class Meta:
        """Global options for Product class."""

        model = Product
        fields = ('product_title', 'product_price', 'product_description',
                  'customer_id', 'product_type_id')


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Convert PaymentType model to JSON"""
    class Meta:
        """Global options for PaymentType class"""
        model = PaymentType
        fields = ('id', 'url', 'customer', 'account_number', 'payment_type_provider')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """Convert ProductType model to JSON"""
    class Meta:
        """Global options for EmployeeTraining class"""
        model = ProductType
        fields = ('product_type', 'product_quantity')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    ''' Convert Order Model to JSON '''
    class Meta:
        """Global Options for Order Class auth:Angela """ 
        model = Order
        fields = ('order_status', 'payment_types_id', 'purchase_customer_id')

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Convert Order-Product model to JSON auth:Angela  """
    class Meta: 
        """ Global options for OrderProduct class """
        model = OrderProduct
        fields = ('product', 'order')
