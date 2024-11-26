from django.db import migrations

def add_initial_products(apps, schema_editor):
    Product = apps.get_model('ecommerce', 'Product')
    Product.objects.create(
        name="Modern Laptop",
        description="High-performance laptop with advanced features.",
        price=899.99,
        stock=50,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584110/cld-sample-5.jpg"
    )
    Product.objects.create(
        name="Wireless Headphones",
        description="Noise-cancelling wireless headphones with superior sound.",
        price=199.99,
        stock=120,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584110/cld-sample-4.jpg"
    )
    Product.objects.create(
        name="Smartphone Pro",
        description="Latest smartphone with cutting-edge features.",
        price=799.99,
        stock=150,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584110/cld-sample-2.jpg"
    )
    Product.objects.create(
        name="4K LED TV",
        description="Ultra HD smart TV with 4K resolution.",
        price=499.99,
        stock=30,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584110/cld-sample.jpg"
    )
    Product.objects.create(
        name="Coffee Mug",
        description="Ceramic coffee mug for everyday use.",
        price=15.99,
        stock=200,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584109/samples/cup-on-a-table.jpg"
    )
    Product.objects.create(
        name="Outdoor Chair",
        description="Comfortable chair for outdoor relaxation.",
        price=89.99,
        stock=80,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584109/samples/man-on-a-street.jpg"
    )
    Product.objects.create(
        name="Dining Table",
        description="Elegant dining table for family gatherings.",
        price=299.99,
        stock=40,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584109/samples/chair-and-coffee-table.jpg"
    )
    Product.objects.create(
        name="Healthy Breakfast",
        description="Nutritious breakfast for a great start to your day.",
        price=19.99,
        stock=150,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584108/samples/breakfast.jpg"
    )
    Product.objects.create(
        name="City Walk",
        description="Perfect shoes for a casual city walk.",
        price=69.99,
        stock=60,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584108/samples/look-up.jpg"
    )
    Product.objects.create(
        name="Birthday Balloons",
        description="A set of colorful balloons for any celebration.",
        price=9.99,
        stock=500,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584108/samples/balloons.jpg"
    )
    Product.objects.create(
        name="Action Camera",
        description="Compact camera perfect for action shots and adventures.",
        price=159.99,
        stock=80,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584654/1731584581042_qigogm.jpg"
    )
    Product.objects.create(
        name="Compact Speaker",
        description="Portable speaker with excellent sound quality.",
        price=49.99,
        stock=250,
        image_url="https://res.cloudinary.com/dghi9xkl0/image/upload/v1731584110/cld-sample-3.jpg"
    )

class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_products),
    ]
