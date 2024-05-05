
from django.db import models

from users.models import User





class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')

    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Дата изменения')

    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создатель')

    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price',)
        permissions = [('can_change_description', 'Can change product description',),
                       ('can_change_category', 'Can change product category',),
                       ('set_published_status', 'Can change product published status',)]


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:

        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title',)
        permissions = [('can_change_publication_sign', 'Can change blog publication_sign',)]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.PositiveIntegerField(verbose_name='номер версии')
    version_name = models.TextField(verbose_name='название версии')
    current_version_indicator = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product}, {self.version_number}, {self.version_name}'

    class Meta:

        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)
