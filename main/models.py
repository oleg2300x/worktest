from django.db import models


class NetworkElement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    products = models.ManyToManyField('Product', related_name='network_elements', verbose_name='Товар')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name}, Товар: {self.products}, Задолженность: {self.debt}'

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} --> {self.release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'