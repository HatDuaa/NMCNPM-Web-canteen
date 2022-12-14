from django.db import models
from django.conf import settings

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

class Comment(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    