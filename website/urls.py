from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from fashionstylish import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fashionstylish.urls')),
    path('accounts/', include('accounts.urls')),

    # path('search/', views.search_view, name='search'),
    # path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
