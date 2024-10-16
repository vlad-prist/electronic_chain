from decimal import Decimal

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    """ Базовая модель с полями создания и изменения. """
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="время последнего изменения")

    class Meta:
        abstract = True


class Contacts(BaseModel):
    """Модель контактов."""
    email = models.EmailField(max_length=100, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}, {self.street}, {self.house_number}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Products(BaseModel):
    """ Модель продуктов. """
    name = models.CharField(max_length=100, verbose_name='наименование')
    model = models.CharField(max_length=100, verbose_name='модель продукта')
    release_date = models.DateField(auto_now_add=False, verbose_name='дата выпуска', help_text='ДД.ММ.ГГГГ')

    def __str__(self):
        """
        Запись '%s: %s' % (self.name, self.model) — это форматирование строки с использованием оператора %,
        где вместо плейсхолдеров %s подставляются значения полей name и model объекта.
        """
        return '%s, %s, %s' % (self.name, self.model, self.release_date)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Factory(BaseModel):
    """ Модель производителя (завода). """
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='address')
    products = models.ManyToManyField(Products)
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='задолженность',
        **NULLABLE
    )

    def __str__(self):
        return f'Производитель: {self.name}, контакты: {self.contacts}'

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'


class Retailer(BaseModel):
    """ Модель розничной сети. """
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='retailer')
    products = models.ManyToManyField(Products)
    provider_factory = models.ForeignKey(
        Factory,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='supplied_retailers'
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='задолженность',
        **NULLABLE
    )

    def __str__(self):
        return f'Розничная сеть: {self.name}, контакты: {self.contacts}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

    def get_provider(self):
        """ Метод определения поставщика. """
        if self.provider_factory:
            return self.provider_factory.name
        return "Нет поставщика"


class Trader(BaseModel):
    """ Модель индивидуальный предприниматель. """
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='trader')
    products = models.ManyToManyField(Products)
    provider_factory = models.ForeignKey(
        Factory,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_for_traders'
    )
    provider_retailer = models.ForeignKey(
        Retailer,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_for_traders'
    )
    debt = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='задолженность'
    )

    def __str__(self):
        return f'Индивидуальный предприниматель: {self.name}, контакты: {self.contacts}'

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'

    def get_provider(self):
        ''' Метод определения поставщика. '''
        if self.provider_factory:
            return self.provider_factory.name
        elif self.provider_retailer:
            return self.provider_retailer.name
        return "Нет поставщика"
