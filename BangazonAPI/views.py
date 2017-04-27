from BangazonAPI.models import *
from rest_framework import viewsets
from BangazonAPI.serializers import *
from BangazonAPI.models import *




class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    Author: Justin Short
    """
    queryset = ProductType.objects.all()
    serializer_class  = ProductTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    Author: Jessica Younker
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    Author: Helana Nosrat
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PaymentTypes to be viewed or edited.
    Author: Max Baldridge
    """
    queryset = PaymentType.objects.all().order_by("payment_type_provider")
    serializer_class = PaymentTypeSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order date to be viewed or edited.
    Author: Angela Less
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited 
    Author: Angela Lee
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

class TrainingCourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows training courses to be viewed or edited 
    Author: Max Baldridge
    """ 
    queryset = TrainingCourse.objects.all()
    serializer_class = TrainingCourseSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited
    Author: Helana Nosrat
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited 
    Author: Angela Lee
    """ 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited
    Author: Angela Lee
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


