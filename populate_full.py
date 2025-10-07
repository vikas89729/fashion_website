import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from fashionstylish.models import Collection, SubCategory, Product

# Sample data
collections_data = [
    {
        "name": "Men's Collection",
        "subcategories": [
            {
                "name": "Shirts",
                "products": [
                    {"name": "Men Shirt 1", "desc": "Nice cotton shirt", "price": 120},
                    {"name": "Men Shirt 2", "desc": "Casual shirt", "price": 150},
                ],
            },
            {
                "name": "Pants",
                "products": [
                    {"name": "Men Pant 1", "desc": "Slim fit pant", "price": 200},
                ],
            },
        ],
    },
    {
        "name": "Women's Collection",
        "subcategories": [
            {
                "name": "Dresses",
                "products": [
                    {"name": "Dress 1", "desc": "Evening gown", "price": 300},
                    {"name": "Dress 2", "desc": "Summer dress", "price": 180},
                ],
            },
            {
                "name": "Tops",
                "products": [
                    {"name": "Top 1", "desc": "Casual top", "price": 90},
                ],
            },
        ],
    },
]

# Create collections, subcategories, and products
for cdata in collections_data:
    collection, _ = Collection.objects.get_or_create(name=cdata["name"], defaults={"desc": "Sample description", "price": 0})
    for sdata in cdata["subcategories"]:
        subcategory, _ = SubCategory.objects.get_or_create(name=sdata["name"], collection=collection)
        for pdata in sdata["products"]:
            Product.objects.get_or_create(
                name=pdata["name"],
                subcategory=subcategory,
                defaults={"desc": pdata["desc"], "price": pdata["price"]}
            )

print("All collections, subcategories, and products created successfully!")
