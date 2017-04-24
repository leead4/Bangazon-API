from BangazonAPI.bangazon.models import Customer
from BangazonAPI.bangazon.models import Product
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """Convert Customer model to JSON"""
    class Meta:
        """Global options for Customer class"""
        model = Customer
        fields = ('firstname', 'lastname', 'status', 'date_created','date_last_active')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Convert Product model to formatted JSON string listing."""

    class Meta:
        """Global options for Product class."""

        model = Product
        fields = ('product_title', 'product_price', 'product_description',
                  'customer_id', 'product_type_id')
