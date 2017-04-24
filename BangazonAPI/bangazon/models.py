from django.db import models


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
