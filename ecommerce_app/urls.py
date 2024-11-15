# ecommerce_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ecommerce import views  # Import views from the ecommerce app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),  # Root URL points to product_list view
    path('ecommerce/', include('ecommerce.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='ecommerce/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ecommerce/logout.html'), name='logout'),
]
