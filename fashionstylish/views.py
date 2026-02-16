from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.http import JsonResponse
from .models import Collection, Product, SubCategory,ContactMessage
from django.contrib.auth.decorators import login_required
from .models import Cart,Order
from .models import Collection, Product, SubCategory, ContactMessage, Cart, Order, ProductVariant, OrderItem
from .models import Product, Banner, FeaturedCollection



# 🟢 Home page
@login_required
def home(request):
    products = Product.objects.all()[:6]  # homepage me latest 4 products
    banners = Banner.objects.filter(active=True)
    collections = FeaturedCollection.objects.filter(is_active=True)[:4]


    context = {
        'products': products,
        'banners': banners,
        'collections': collections,
    }
    return render(request, 'fashionstylish/index.html', context)
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.variant.price * item.quantity for item in cart_items)
    return render(request, 'fashionstylish/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

def order_success(request):
    return render(request, 'fashionstylish/order_success.html')


from django.db.models import Q
from .models import Product

def search(request):
    query = request.GET.get('q')
    results = Product.objects.none()

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(desc__icontains=query)
        )

    return render(request, 'fashionstylish/search_results.html', {
        'query': query,
        'results': results
    })





def search_suggestions(request):
    q = request.GET.get('q', '').strip()
    suggestions = []
    if q:
        qs = Product.objects.filter(
            Q(name__icontains=q) | Q(desc__icontains=q)
        ).values('id', 'name')[:6]
        suggestions = list(qs)
    return JsonResponse({'suggestions': suggestions})



def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'fashionstylish/collection_list.html', {'collections': collections})



def subcategory_list(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    subcategories = collection.subcategories.all()
    return render(request, 'fashionstylish/subcategory_list.html', {
        'collection': collection,
        'subcategories': subcategories
    })



def product_list(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    products = subcategory.products.all()
    return render(request, 'fashionstylish/product_list.html', {
        'subcategory': subcategory,
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # 🔹 Fetch all variants of this product
    variants = product.variants.all()

    # 🔹 Related products from same subcategory (excluding current)
    related_products = Product.objects.filter(
        subcategory=product.subcategory
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'variants': variants,
        'related_products': related_products,
    }
    return render(request, 'fashionstylish/product_detail.html', context)





def about(request):
    return render(request, 'fashionstylish/about.html')


# Contact page
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        #  Save the data to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        #  Optional: show a success message
        return render(request, 'fashionstylish/contact.html', {'success': True})

    #  For GET request — just show the form
    return render(request, 'fashionstylish/contact.html')




@login_required
def add_to_cart(request, variant_id):
    variant = get_object_or_404(ProductVariant, id=variant_id)

    quantity = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1

    cart_item, created = Cart.objects.get_or_create(user=request.user, variant=variant)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect('view_cart')



@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.variant.price * item.quantity for item in cart_items)
    return render(request, 'fashionstylish/cart.html', {'cart_items': cart_items, 'total': total})




@login_required
def remove_from_cart(request, variant_id):
    item = get_object_or_404(Cart, user=request.user, variant_id=variant_id)
    item.delete()
    return redirect('view_cart')

@login_required
def place_order(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.variant.price * item.quantity for item in cart_items)
        cart_items = Cart.objects.filter(user=request.user)
        print("Cart Count:", cart_items.count())

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            city=city,
            zip_code=zip_code,
            phone=phone,
            total_price=total_price
        )

        # Save individual items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                variant=item.variant,
                quantity=item.quantity,
                price=item.variant.price
            )

        cart_items.delete()
        return redirect('order_success')

    return redirect('checkout')


@login_required
def profile(request):
    orders_count = Order.objects.filter(user=request.user).count()
    return render(request, 'fashionstylish/profile.html', {
        'orders_count': orders_count
    })


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'fashionstylish/order_history.html', {'orders': orders})
def collection_products(request, pk):
    collection = Collection.objects.get(pk=pk)
    products = Product.objects.filter(subcategory__collection=collection)

    return render(request, 'fashionstylish/collection_products.html', {
        'collection': collection,
        'products': products
    })
