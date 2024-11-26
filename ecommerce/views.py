from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Order, OrderItem
from .forms import ProductForm, UserRegisterForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import logout

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser  # Only admin users can access these views

# Product List View (accessible by all users)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

# Add Product (restricted to admin users)
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'ecommerce/add_product.html', {'form': form})

# Edit Product (restricted to admin users)
@user_passes_test(is_admin)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'ecommerce/edit_product.html', {'form': form, 'product': product})

# Delete Product (restricted to admin users)
@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'ecommerce/delete_product.html', {'product': product})

# Register new user (open to all users)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'ecommerce/register.html', {'form': form})

# Cart View (login required, or show message to log in)
def view_cart(request):
    if not request.user.is_authenticated:
        # Display a message telling the user to log in
        messages.info(request, 'Please log in to view your cart.')
        return redirect('login')  # Redirect to login page

    # If logged in, show the cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'ecommerce/cart.html', {'cart': cart})

# Add to Cart (login required)
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'{product.name} added to cart!')
    return redirect('view_cart')
#add quantity
@login_required
def update_cart_quantity(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)

        # Loop through the form items and update the quantities
        for key, value in request.POST.items():
            if key.startswith('quantity_'):  # Look for fields that start with 'quantity_'
                product_id = key.split('_')[1]  # Extract the product_id from the field name
                try:
                    product = Product.objects.get(id=product_id)
                    quantity = int(value)  # Get the quantity value
                    cart_item = CartItem.objects.get(cart=cart, product=product)
                    cart_item.quantity = quantity
                    cart_item.save()
                except (Product.DoesNotExist, CartItem.DoesNotExist):
                    continue

        messages.success(request, "Your cart has been updated.")
        return redirect('view_cart')

    return redirect('view_cart')

# Remove from Cart (login required)
@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    messages.success(request, f'{product.name} removed from cart!')
    return redirect('view_cart')

# Place an Order (login required)
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        return redirect('view_cart')

    # Create a new order
    order = Order.objects.create(user=request.user)
    total_amount = 0

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        total_amount += item.product.price * item.quantity

    # Update order total amount and mark as completed
    order.total_amount = total_amount
    order.is_completed = True
    order.save()

    # Clear the cart
    cart.items.all().delete()

    messages.success(request, 'Your order has been placed successfully!')
    return render(request, 'ecommerce/order_success.html', {'order': order})

# View Orders (login required)
@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'ecommerce/orders.html', {'orders': orders})

# Custom Logout View
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Redirect to the login page or homepage
