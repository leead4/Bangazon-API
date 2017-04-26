from django.db import models


class ProductType(models.Model):
    """
    This class defines a ProductType in a table of producttypes.
    Author: Justin Short
    
    The response will be a producttype details response object.

    Keyword Methods:
    Product_type: string, the name of the prodcut type
    Product_quantity: integer, how many of a product exists
    """
    product_type = models.CharField(max_length=45)
    product_quantity = models.IntegerField(default=0) # This will be used to show amount of products in each type

    def __str__(self):
        return "{}'s have {} amount of products".format(self.product_type, self.product_quantity)


class Customer(models.Model):
    """
    This class defines a Customer in a table of customers.
    Author: Jessica Younker
    
    The response will be a product details response object.

    Keyword Methods:
    First_name: string, the first name of the customer
    Last_name: string, the last name of the customer
    Date_created: datetime, the date the customer's account was created
    Date_last_active: datetime, the date the customer last accessed their account
    """
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_created = models.DateField(auto_now_add=True)
    date_last_active = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)

    def customer_status(self):
        """
        method determining if status is active or inactive (no login within 240 days)
        Author: Jessica Younker
        """
        days_inactive = date_last_active - date_created
        if days_inactive.days <= 239:
            self.status = "active"
        else: self.status = "inactive"

    def __str__(self):
        """
        convert Customer object to readable string
        Author: Jessica Younker
        """
        return "{} {}".format(self.firstname, self.lastname)


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

    product_title = models.CharField(max_length=25)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customer)
    product_type_id = models.ForeignKey(ProductType)

    def __str__(self):
        """
        Return a string listing product fields.
        Interacts with admin interface.
        """
        return "{} {}".format(self.product_title, self.product_price, self.product_description)

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

class OrderProduct(models.Model):
    """
    This class defines a relationship between Orders and Products in a table of orderproducts.
    Author: Angela Lee
    
    The response will be a orderproduct relationship details response object.

    Keyword Methods:
    Order_id: foreign key identifier for order in orderproduct
    Product_id: foreign key identifier for Product in orderproduct
    """ 
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)



















