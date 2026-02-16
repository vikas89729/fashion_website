from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import uuid

class Collection(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.CharField(max_length=110)
    image = models.ImageField(upload_to="collections/", null=True, blank=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="subcategories/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.collection.name})"


class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def starting_price(self):
        prices = self.variants.values_list('price', flat=True)
        return min(prices) if prices else None

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    def __str__(self):
        return f"{self.product.name} - {self.size or ''} {self.color or ''}".strip()
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.variant} ({self.quantity})"

    @property
    def total_price(self):
        return self.variant.price * self.quantity


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey("ProductVariant", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.variant} ({self.quantity})"



class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)  # link for SHOP NOW button
    active = models.BooleanField(default=True)  # only show active banners

    def __str__(self):
        return self.title or "Banner"

class FeaturedCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)


    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.collection.name



