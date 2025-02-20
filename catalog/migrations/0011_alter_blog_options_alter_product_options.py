# Generated by Django 4.2.2 on 2024-05-01 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_product_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('title',), 'permissions': [('can_change_publication_sign', 'Can change blog publication_sign')], 'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('price',), 'permissions': [('can_change_description', 'Can change product description'), ('can_change_category', 'Can change product category')], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
