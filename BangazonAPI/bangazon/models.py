from django.db import models


class Customer(models.Model):
    """
    class defining Customer table in database
    """
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    date_created = models.DateField(auto_now_add=True)
    date_last_active = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)


    # def customer_status():
    #     """
    #     method determining if status is active or inactive (after 239 days)
    #     """
    #     days_inactive = date_last_active - date_created
    #     if days_inactive.days <= 239:
    #         status = "active"
    #     else: status = "inactive"
    #     return status


    def __str__(self):
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
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=25)
    customer_id = models.ForeignKey(Customer)
    product_type_id = models.ForeignKey(Product_Type)

    def __str__(self):
        """Return a string listing product fields.

        Interacts with admin interface.
        """
        return "{} {}".format(self.product_title, self.product_price,
                              self.product_description)
