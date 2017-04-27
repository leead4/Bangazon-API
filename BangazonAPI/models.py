from django.db import models


class ProductType(models.Model):
    """
    This class defines a ProductType in a table of producttypes.
    Author: Justin Short

    The response will be a producttype details response object.

    Keyword Methods:
    Product_type: string, the name of the product type
    Product_quantity: integer, how many of a product exists
    """
    product_type = models.CharField(max_length=45)
    product_quantity = models.IntegerField(default=0) # This will be used to show amount of products in each type

    def __str__(self):
        return "{} : {}-count".format(self.product_type, self.product_quantity)


def set_customer_status(customer):
    customer.status = 'ACTIVE'


class Customer(models.Model):
    """
    This class defines a Customer in a table of customers.
    Author: Jessica Younker

    The response will be a product details response object.

    Keyword Methods:
    first_name: string, the first name of the customer
    last_name: string, the last name of the customer
    date_created: datetime, the date the customer's account was created
    date_last_active: datetime, the date the customer last accessed their account
    status_options_choices: active or inactive, selected from dropdown
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_created = models.DateField(auto_now_add=True)
    date_last_active = models.DateField(auto_now_add=True)
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    STATUS_OPTIONS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )
    status = models.CharField(max_length=8, choices=STATUS_OPTIONS_CHOICES, default=ACTIVE)

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{} {}".format(self.first_name, self.last_name)


class Product(models.Model):
    """
    This class defines a Product in a table of products.
    Author: Helana Nosrat

    The response will be a product details response object.

    Keyword Methods:
    Title: string, product name
    Price: string, price of product in US dollars
    Description: string, a description of the product
    Customer_id: foreign key identifier for customers in products
    Product_type_id: foreign key identifier for product types in products
    """

    title = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer)
    product_type_id = models.ForeignKey(ProductType)

    def __str__(self):
        """
        Return a string listing product fields.
        Interacts with admin interface.
        """
        return "{} {}".format(self.title, self.price, self.description)

class PaymentType(models.Model):
    """
    This class defines a Payment Type in a table of products.
    Author: Max Baldridge

    The response will be a payment type details response object.

    Keyword Methods:
    Payment_Type_Provider: string, Credit/Debit Card Company, or Bank/Check
    Account_number: string, a string of numbers and/or letters
    Customer_id: foreign key identifier for customers in products
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="payment_types",
        related_query_name="payment_types"
    )
    payment_type_provider = models.CharField(max_length=25)
    account_number = models.CharField(max_length=25)

    def __str__(self):
        """
        Return a string listing product fields.
        Interacts with admin interface.
        """
        return "{}".format(self.payment_type_provider)

class Order(models.Model):
    """
    This class defines a Order in a table of orders.
    Author: Angela Lee

    The response will be a order details response object.

    Keyword Methods:
    Order_Status: string, whether or not the order is active
    Payment_types_id: foreign key identifier for payment types in orders
    Purchase_customer_id: foreign key identifier for customers in orders
    """

    order_status = models.CharField(max_length = 25)
    payment_types_id = models.ForeignKey(PaymentType)
    purchase_customer_id = models.ForeignKey(Customer)

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{}'s' order is {}".format(self.purchase_customer_id, self.order_status)

class OrderProduct(models.Model):
    """
    This class defines a relationship between Orders and Products in a table of orderproducts.
    Author: Angela Lee

    The response will be a orderproduct relationship details response object.

    Keyword Methods:
    Order_id: foreign key identifier for order in orderproduct
    Product_id: foreign key identifier for Product in orderproduct
    """ 
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)


class TrainingCourse(models.Model):
    """
    This class defines a Training Course in a table of training courses
    Author: Max Baldridge
    
    The response will be a training course details response object.

    Keyword Methods:
    Course_name: string, the name of the raining course
    Start_date: string, the date the course starts
    End_date: string, the date the course ends
    Max_capacity: string, shows the maximum number of employees that can attend the
    """

    course_name = models.CharField(max_length = 25)
    start_date = models.CharField(max_length = 25)
    end_date = models.CharField(max_length = 25)
    max_capacity = models.CharField(max_length = 25)

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{}".format(self.course_name)

class Department(models.Model):
    """
    This class defines a department in a table of multiple Departments.
    Author: Helana Nosrat

    The response will be a department detail response object.

    Keyword Methods:
    department_name: a string providing a department name
    expense_budget: a string providing a departments alotted expense budget in US dollars.

    """

    name = models.CharField(max_length=25)
    expense_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{}".format(self.name)

class Employee(models.Model):
    """
    This class defines a Employee in a table of employees.
    Author: Jessica Younker

    The response will be a employee details response object.

    Keyword Methods:
    first_name: string, the first name of the employee
    last_name: string, the last name of the employee
    title: employee title
    department_id: foreign key identifier for Employee in Deparment
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    department_id = models.ForeignKey(Department)
    

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{} {}".format(self.first_name, self.last_name)
