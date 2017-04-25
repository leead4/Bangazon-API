from django.db import models


class ProductType(models.Model):
    """
    class defining ProductType table in database
    Author: Justin Short
    """
    product_type = models.CharField(max_length=45)
    product_quantity = models.IntegerField(default=0) # This will be used to show amount of products in each type

    def __str__(self):
        return "{}'s have {} amount of products".format(self.product_type, self.product_quantity)


class Customer(models.Model):
    """
    class defining Customer table in database
    Author: Jessica Younker
    """
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
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
    """This class defines a Product in a table of products.

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
    product_type_id = models.ForeignKey(Product_Type)

    def __str__(self):
        """Return a string listing product fields.

        Interacts with admin interface.
        """
        return "{} {}".format(self.product_title, self.product_price, self.product_description)

class PaymentType(models.Model):
    """
    class defining Payment Type table in database
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
'''
class defining Order table in database auth:Angela 
'''
    status_active = models.CharField(auto_now_add=False)
    payment_types_id = models.ForeignKey(PaymentType)
    purchase_customer_id = models.ForeignKey(Customer)

class OrderProduct(models.Model):
    """ class defining Order Product relational data in Database """ 
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)