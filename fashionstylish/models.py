from django.db import models
from django.utils.safestring import mark_safe


class Collection(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=110)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="collections/", null=True, blank=True)


    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="subcategories")
    image = models.ImageField(upload_to="SubCategory/", null=True, blank=True)


    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=110, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="Product/", null=True, blank=True)


    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"

    def __str__(self):
        return self.name
