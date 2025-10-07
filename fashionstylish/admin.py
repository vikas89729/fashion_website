from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Collection,SubCategory,Product

# Collection admin
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'image_tag')
    search_fields = ('name', 'desc')
    list_filter = ('price',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"
    image_tag.short_description = 'Image Preview'


# SubCategory admin
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'image_tag')
    search_fields = ('name',)
    list_filter = ('collection',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"
    image_tag.short_description = 'Image Preview'


# Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price', 'image_tag')
    search_fields = ('name', 'desc')
    list_filter = ('subcategory', 'price')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;"/>')
        return "No Image"
    image_tag.short_description = 'Image Preview'
