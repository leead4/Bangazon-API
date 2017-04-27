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
        fields = ('first_name', 'last_name', 'status', 'date_created','date_last_active')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Product model to formatted JSON string listing.
    Author: Helana Nosrat
    """

    class Meta:
        """Global options for Product class."""

        model = Product
        fields = ('title', 'price', 'description',
                  'customer', 'product_type')


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert PaymentType model to JSON
    Author: Max Baldridge
    """
    class Meta:
        """Global options for PaymentType class"""
        model = PaymentType
        fields = ('id', 'url', 'customer', 'account_number', 'payment_type_provider')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert ProductType model to JSON
    Author: Justin Short
    """
    class Meta:
        """Global options for EmployeeTraining class"""
        model = ProductType
        fields = ('product_type', 'product_quantity')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Order Model to JSON
    Author: Angela Lee
    """
    class Meta:
        """Global Options for Order Class auth:Angela """
        model = Order
        fields = ('order_status', 'payment_types', 'purchase_customer')

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Order-Product model to JSON
    Author: Angela Lee
    """
    class Meta:
        """ Global options for OrderProduct class """
        model = OrderProduct
        fields = ('product', 'order')

class TrainingCourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert TraingCourse model to JSON 
    Author: Max Baldridge
    """
    class Meta: 
        """ Global options for OrderProduct class """
        model = TrainingCourse
        fields = ('course_name', 'start_date', 'end_date', 'max_capacity')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Department Data to JSON
    Author: Helana
    """
    class Meta:
        """ Global options for Department class """
        model = Department
        fields = ('name', 'expense_budget')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Convert Order-Product model to JSON 
    Author: Angela Lee
    """
    class Meta: 
        """ Global options for OrderProduct class """
        model = Employee
        fields = ('first_name', 'last_name', 'title', 'department')
