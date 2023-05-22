from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ["age"]

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True, )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
    