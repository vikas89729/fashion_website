import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from fashionstylish.models import Collection, SubCategory, Product

# Sample data with image paths
collections_data = [
    {
        "name": "Men's Collection",
        "desc": "Exclusive men's fashion",
        "price": 0,
        "image": "collections/mens_collection.jpg",
        "subcategories": [
            {
                "name": "Shirts",
                "image": "SubCategory/mens_shirts.jpg",
                "products": [
                    {"name": "Men Shirt 1", "desc": "Nice cotton shirt", "price": 120, "image": "Product/men_shirt1.jpg"},
                    {"name": "Men Shirt 2", "desc": "Casual shirt", "price": 150, "image": "Product/men_shirt2.jpg"},
                ],
            },
            {
                "name": "Pants",
                "image": "SubCategory/mens_pants.jpg",
                "products": [
                    {"name": "Men Pant 1", "desc": "Slim fit pant", "price": 200, "image": "Product/men_pant1.jpg"},
                ],
            },
        ],
    },
    {
        "name": "Women's Collection",
        "desc": "Trendy women's fashion",
        "price": 0,
        "image": "collections/womens_collection.jpg",
        "subcategories": [
            {
                "name": "Dresses",
                "image": "SubCategory/womens_dresses.jpg",
                "products": [
                    {"name": "Dress 1", "desc": "Evening gown", "price": 300, "image": "Product/dress1.jpg"},
                    {"name": "Dress 2", "desc": "Summer dress", "price": 180, "image": "Product/dress2.jpg"},
                ],
            },
            {
                "name": "Tops",
                "image": "SubCategory/womens_tops.jpg",
                "products": [
                    {"name": "Top 1", "desc": "Casual top", "price": 90, "image": "Product/top1.jpg"},
                ],
            },
        ],
    },
]

# Create collections, subcategories, and products
for cdata in collections_data:
    collection, _ = Collection.objects.get_or_create(
        name=cdata["name"],
        defaults={"desc": cdata["desc"], "price": cdata["price"], "image": cdata["image"]}
    )
    for sdata in cdata["subcategories"]:
        subcategory, _ = SubCategory.objects.get_or_create(
            name=sdata["name"],
            collection=collection,
            defaults={"image": sdata["image"]}
        )
        for pdata in sdata["products"]:
            Product.objects.get_or_create(
                name=pdata["name"],
                subcategory=subcategory,
                defaults={"desc": pdata["desc"], "price": pdata["price"], "image": pdata["image"]}
            )

print("All collections, subcategories, and products (with images) created successfully!")

