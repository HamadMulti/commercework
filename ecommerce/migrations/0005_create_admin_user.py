
from django.db import migrations

def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='vero3').exists():  # You can replace 'admin' with your desired username
        User.objects.create_superuser('vero3', 'admin@vero.com', 'Vero88')  # Replace with desired credentials

class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_product_image_alter_product_created_at_and_more'),  # Keep this as it is
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
