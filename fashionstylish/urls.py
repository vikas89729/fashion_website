from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    #  Collections → Subcategory → Product → Product Detail
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:pk>/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/<int:pk>/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('collection/<int:pk>/', views.collection_products, name='collection_products'),


    # Cart
    path('add_to_cart/<int:variant_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:variant_id>/', views.remove_from_cart, name='remove_from_cart'),

    #  Checkout & Order
    path('checkout/', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),

    #  Static pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    #  Search
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),

path('my-orders/', views.order_history, name='order_history'),

]
