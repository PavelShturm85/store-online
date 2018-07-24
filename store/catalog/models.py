from django.db import models
import uuid
from PIL import Image
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('catalog:ProductListByCategory', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to='uploads')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    specification = models.TextField(
        verbose_name='Описание товара', blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, blank=True, null=True)
    stock = models.PositiveIntegerField(verbose_name="На складе")

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = [
            ['id', 'slug']
        ]

    def get_absolute_url(self):
        return reverse('catalog:ProductDetail', args=[self.id, self.slug])

    def __str__(self):
        return '{} {}'.format(self.name, self.price)
