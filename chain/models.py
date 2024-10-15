from django.db import models


NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    """Базовая модель с полями создания и изменения."""
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
    office = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}, {self.street}, {self.office}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Products(BaseModel):
    """ Модель продуктов. """
    name = models.CharField(max_length=100, verbose_name='наименование')
    model = models.CharField(max_length=100, verbose_name='модель продукта')
    release_date = models.DateField(auto_now_add=False, verbose_name='дата выпуска', help_text='ДД.ММ.ГГГГ')

    def __str__(self):
        return f'{self.name}, {self.model}, {self.release_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Factory(BaseModel):
    """Модель завод."""
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='address')
    products = models.ManyToManyField(Products)
    debt = models.FloatField(default=0.00, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.contacts}, {self.products}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class Retailer(BaseModel):
    """Модель розничной сети."""
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='retailer')
    products = models.ManyToManyField(Products)
    provider_factory = models.ForeignKey(
        Factory,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_retailers'
    )
    provider_retailer = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_retailers'
    )
    provider_trader = models.ForeignKey(
        'Trader',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_retailers'
    )
    debt = models.FloatField(default=0.00, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.contacts}, {self.products}'

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

    def get_provider(self):
        return self.provider_factory.name or self.provider_retailer.name or self.provider_trader.name


class Trader(BaseModel):
    """Модель индивидуальный предприниматель."""
    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, related_name='trader')
    products = models.ManyToManyField(Products)
    # factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='traders')
    provider_factory = models.ForeignKey(
        Factory,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_traders'
    )
    provider_retailer = models.ForeignKey(
        Retailer,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_traders'
    )
    provider_trader = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='provider_traders'
    )
    debt = models.FloatField(default=0.00, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.contacts}, {self.products}'

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальные предприниматели'

    def get_provider(self):
        return self.provider_factory.name or self.provider_retailer.name or self.provider_trader.name
