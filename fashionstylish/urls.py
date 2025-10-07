from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('collections/', views.collection_list, name='collection_list'),  # Correct view function
    path('collection/<int:pk>/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/<int:pk>/', views.product_list, name='product_list'),
    # Correct version
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    path('search/', views.search_view, name='search'),
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),


]