from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Catigory Name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Product Name')
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    describtion = models.TextField(verbose_name='Describtion', null=True)

