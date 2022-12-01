from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=200)
    #body = models.TextField()
    type = models.CharField(max_length=200, null=True)
    remaining = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    image = models.ImageField(null=True)


    def _str_(self):
        return self.name