from rest_framework import serializers
from chain.models import Contacts, Products, Factory, Retailer, Trader
from chain.validators import validate_debt


class BaseSerializer(serializers.ModelSerializer):
    """
    Базовый сериалайзер для корректного отображения даты и времени создания и обновления.
    """
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        abstract = True
        fields = ('created_at', 'updated_at')


class ContactsSerializer(BaseSerializer):
    """ Сериалайзер модели Contacts. """

    class Meta:
        model = Contacts
        fields = ('id', 'email', 'country', 'city', 'street', 'house_number',)


class ProductsSerializer(BaseSerializer):
    """ Сериалайзер модели Products. """
    release_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Products
        fields = ('id', 'name', 'model', 'release_date',)


class FactorySerializer(BaseSerializer):
    """ Сериалайзер модели Factory. """
    products_name_only = serializers.SerializerMethodField()
    contacts_readable = serializers.SerializerMethodField()

    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts_readable', 'products_name_only', 'created_at',)
        read_only_fields = ('created_at',)

    def get_products_name_only(self, obj):
        return [product.name for product in obj.products.all()]

    def get_contacts_readable(self, obj):
        return (f"email: {obj.contacts.email}. "
                f"Адрес: {obj.contacts.country}, г.{obj.contacts.city}, "
                f"{obj.contacts.street}, {obj.contacts.house_number}.")


class RetailerSerializer(BaseSerializer):
    """ Сериалайзер модели Retailer. """
    products_name_only = serializers.SerializerMethodField()
    contacts_readable = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[validate_debt]
    )

    class Meta:
        model = Retailer
        fields = ('id', 'name', 'contacts_readable', 'provider', 'products_name_only', 'debt', 'created_at',)
        read_only_fields = ('created_at',)

    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        return "Нет поставщика"

    def get_products_name_only(self, obj):
        return [product.name for product in obj.products.all()]

    def get_contacts_readable(self, obj):
        return (f"email: {obj.contacts.email}. "
                f"Адрес: {obj.contacts.country}, г.{obj.contacts.city}, "
                f"{obj.contacts.street}, {obj.contacts.house_number}.")


class TraderSerializer(BaseSerializer):
    products_name_only = serializers.SerializerMethodField()
    contacts_readable = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    debt = serializers.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[validate_debt]
    )

    class Meta:
        model = Trader
        fields = ('id', 'name', 'contacts_readable', 'provider', 'products_name_only', 'debt', 'created_at',)
        read_only_fields = ('created_at',)

    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        elif obj.provider_retailer:
            return obj.provider_retailer.name
        return "Нет поставщика"

    def get_products_name_only(self, obj):
        return [product.name for product in obj.products.all()]

    def get_contacts_readable(self, obj):
        return (f"email: {obj.contacts.email}. "
                f"Адрес: {obj.contacts.country}, г.{obj.contacts.city}, "
                f"{obj.contacts.street}, {obj.contacts.house_number}.")