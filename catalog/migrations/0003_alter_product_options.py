# Generated by Django 5.0.3 on 2024-03-20 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('price',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
