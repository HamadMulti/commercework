from django.contrib import admin
from .models import Product, Cart, CartItem, Order, OrderItem
from django.utils.html import format_html

# Customizing the admin for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at', 'image_preview')  # Added image_preview
    search_fields = ['name', 'description']  # Fields that can be searched
    list_filter = ['created_at', 'price']  # Filters to be displayed
    ordering = ['-created_at']  # Default ordering by created date
    fields = ('name', 'description', 'price', 'stock', 'image', 'image_url')  # Fields to show in form

    def image_preview(self, obj):
        # If an image_url exists, display the image from the URL
        if obj.image_url:
            return format_html('<img src="{}" style="width: 50px; height: auto;">', obj.image_url)
        # Otherwise, display the locally uploaded image (if available)
        elif obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;">', obj.image.url)
        return ""
    image_preview.short_description = 'Image Preview'

admin.site.register(Product, ProductAdmin)

# Customizing the admin for Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Columns to display
    search_fields = ['user__username']  # Searching by user username

admin.site.register(Cart, CartAdmin)

# Customizing the admin for CartItem model
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')  # Columns to display
    search_fields = ['cart__user__username', 'product__name']  # Searching by user username and product name
    list_filter = ['cart__user']  # Filtering by user
    raw_id_fields = ('cart', 'product')  # Use raw IDs to avoid long dropdowns

admin.site.register(CartItem, CartItemAdmin)

# Customizing the admin for Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_amount', 'is_completed')  # Columns to display
    search_fields = ['user__username']  # Searching by user username
    list_filter = ['is_completed', 'created_at']  # Filters for completion and date
    list_editable = ['is_completed']  # Allow editing completion status directly in the list view

admin.site.register(Order, OrderAdmin)

# Customizing the admin for OrderItem model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')  # Columns to display
    search_fields = ['order__user__username', 'product__name']  # Searching by user username and product name
    list_filter = ['order__is_completed']  # Filtering by order completion status
    raw_id_fields = ('order', 'product')  # Use raw IDs for order and product

admin.site.register(OrderItem, OrderItemAdmin)
