from django.db import models

# Create your models here.
class Booking(models.Model):
    """
    This class is mapping the booking table and
    his attributes
    """
    name = models.CharField(max_length=255)
    guests_number = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    """
    This class is mapping Menu table and
    his attributes
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    def get_item(self):
        """This method return a created menu
        item in string datatype"""
        return f'{self.title} : {self.price}'
