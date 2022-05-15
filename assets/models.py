from django.db import models

# Create your models here.
# create a model for categories
class Categories(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
    
# create a model for assets
class Assets(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serial_No = models.CharField(max_length=16, unique=True, )
    barcode = models.CharField(max_length=16, unique=True, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
    # define model plural name
    class Meta:
        verbose_name_plural = 'Assets'


