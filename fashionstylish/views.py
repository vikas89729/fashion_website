from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from .models import Collection, Product, SubCategory


# 🟢 Home page
def home(request):
    return render(request, 'fashionstylish/index.html')


# 🟢 Search view (shows results)
def search_view(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(desc__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'fashionstylish/search_results.html', context)
    # 👆 Make sure your template path matches this (see below)


# 🟢 Live suggestions for AJAX search
def search_suggestions(request):
    q = request.GET.get('q', '').strip()
    suggestions = []
    if q:
        qs = Product.objects.filter(
            Q(name__icontains=q) | Q(desc__icontains=q)
        ).values('id', 'name')[:6]
        suggestions = list(qs)
    return JsonResponse({'suggestions': suggestions})


# 🟢 Show all collections
def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'fashionstylish/collection_list.html', {'collections': collections})


# 🟢 Show subcategories for a collection
def subcategory_list(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    subcategories = collection.subcategories.all()
    return render(request, 'fashionstylish/subcategory_list.html', {
        'collection': collection,
        'subcategories': subcategories
    })


# 🟢 Show products for a subcategory
def product_list(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    products = subcategory.products.all()
    return render(request, 'fashionstylish/product_list.html', {
        'subcategory': subcategory,
        'products': products
    })


# 🟢 Show product details
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'fashionstylish/product_detail.html', {'product': product})


# 🟢 About page
def about(request):
    return render(request, 'fashionstylish/about.html')


# 🟢 Contact page
def contact(request):
    return render(request, 'fashionstylish/contact.html')
# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return render(request, 'fashionstylish/product_detail.html', {'product': product})

