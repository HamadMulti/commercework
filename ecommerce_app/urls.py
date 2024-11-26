from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ecommerce import views  # Import views from the ecommerce app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),  # Root URL points to product_list view
    path('ecommerce/', include('ecommerce.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='ecommerce/login.html'), name='login'),
    
    # Updated Logout URL without custom template
    path('logout/', views.custom_logout, name='logout'),  # URL for custom logout  

    # Password Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='ecommerce/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='ecommerce/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='ecommerce/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='ecommerce/password_reset_complete.html'), name='password_reset_complete'),
]
