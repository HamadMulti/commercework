from django.urls import path
from . import views  # Import your views
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in auth views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('cart/update/', views.update_cart_quantity, name='update_cart'),

    # User Registration URL
    path('register/', views.register, name='register'),

    # Cart URLs
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Fixed missing comma

    # Order URLs
    path('order/place/', views.place_order, name='place_order'),
    path('orders/', views.view_orders, name='view_orders'),

    # Login and Logout URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
