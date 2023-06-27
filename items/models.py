from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.category} {self.brand} {self.model}'
    
