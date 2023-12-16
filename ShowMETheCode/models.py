from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator , MaxValueValidator

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return str(self.name)

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    brand = models.OneToOneField(Brand, related_name='accessories', on_delete=models.CASCADE)
    category = models.OneToOneField(Category, related_name='accessories', on_delete=models.CASCADE)
    material = models.OneToOneField(Material, related_name='accessories', on_delete=models.CASCADE, blank=True, null=True)
    color = models.OneToOneField(Color, related_name='accessories', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='accessories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    discount = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], help_text="Percentage of the discount")
    slug = models.SlugField(max_length=150, unique=True, blank=True, allow_unicode=True, verbose_name='آدرس لینک')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True) if not self.slug else self.slug
        self.is_available = self.stock > 0 
        super().save(*args, **kwargs)

    def purchase(self, quantity):
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if self.stock >= quantity:
            self.stock -= quantity
            self.save(update_fields=['stock'])
            return True
        else:
            raise ValueError("Not enough stock to complete purchase.")

    def get_discounted_price(self):
        if not self.discount:
            return self.price
        return self.price * (1 - self.discount / 100.0)

    @property
    def is_on_sale(self):
        return self.discount > 0
