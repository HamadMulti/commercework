# ecommerce_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ecommerce import views  # Import views from your ecommerce app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),  # Homepage displays product list
    path('ecommerce/', include('ecommerce.urls')),  # Include URLs from the ecommerce app
]

# Serve media files during development (for handling uploaded images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
