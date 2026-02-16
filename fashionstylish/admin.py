from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Banner
from .models import (
    Collection, SubCategory,
    Product, ProductVariant,
    Order, OrderItem,FeaturedCollection
)

# ================= COLLECTION =================
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" height="80" '
                f'style="object-fit:cover; border-radius:5px;" />'
            )
        return "No Image"

    image_tag.short_description = 'Image Preview'


# ================= SUBCATEGORY =================
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'collection', 'image_tag')
    search_fields = ('name',)
    list_filter = ('collection',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" height="80" '
                f'style="object-fit:cover; border-radius:5px;" />'
            )
        return "No Image"

    image_tag.short_description = 'Image Preview'


# ================= PRODUCT VARIANT INLINE =================
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    fields = ('color', 'size', 'price', 'stock', 'sku')
    readonly_fields = ('sku',)


# ================= PRODUCT =================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'starting_price', 'image_tag')
    search_fields = ('name',)
    list_filter = ('subcategory',)
    readonly_fields = ('image_tag',)
    inlines = [ProductVariantInline]

    def starting_price(self, obj):
        prices = obj.variants.values_list('price', flat=True)
        return min(prices) if prices else "-"

    starting_price.short_description = "Starting Price"

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" height="80" '
                f'style="object-fit:cover; border-radius:5px;" />'
            )
        return "No Image"

    image_tag.short_description = 'Image Preview'


# ================= ORDER ITEM INLINE =================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


# ================= ORDER =================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'city', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('user__username', 'full_name', 'phone')
    inlines = [OrderItemInline]


# ================= ORDER ITEM =================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'variant', 'quantity', 'price')
    search_fields = ('order__id', 'variant__product__name')
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'active')
    list_filter = ('active',)
    search_fields = ('title',)

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="120" />')
        return "No Image"

    preview.short_description = "Preview"

@admin.register(FeaturedCollection)
class FeaturedCollectionAdmin(admin.ModelAdmin):
    list_display = ('collection', 'is_active')
    list_filter = ('is_active',)
