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
    