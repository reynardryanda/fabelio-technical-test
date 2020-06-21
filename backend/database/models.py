from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class MSTProduct(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(999999999)])
    dimension = models.CharField(max_length=15)
    material = models.CharField(max_length=20)
    max_seats = models.IntegerField(validators=[MinValueValidator(1)])
    image_url = models.URLField()

    class Meta:
        db_constraints = {
            'price_above_zero': 'check (price>0)',
            'max_seats_above_zero': 'check (max_seats>0)',
        }

class TRXProduct(models.Model):
    mst_product = models.ForeignKey(MSTProduct, related_name="details",on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ["mst_product","color"]
        db_constraints = {
            'quantity_not_negative': 'check (quantity>=0)',
        }