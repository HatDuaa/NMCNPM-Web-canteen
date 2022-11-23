from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=1)

    def _str_(self):
        return self.title