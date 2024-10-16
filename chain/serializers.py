from rest_framework import serializers
from chain.models import Contacts, Products, Factory, Retailer, Trader


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
        fields = ('id', 'email', 'country', 'city', 'street', 'office',)


class ProductsSerializer(BaseSerializer):
    """ Сериалайзер модели Products. """
    release_date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Products
        fields = ('id', 'name', 'model', 'release_date',)


class FactorySerializer(BaseSerializer):
    """ Сериалайзер модели Factory. """
    products = ProductsSerializer(many=True)
    contacts = ContactsSerializer()

    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts', 'products', 'created_at',)


class RetailerSerializer(BaseSerializer):
    """ Сериалайзер модели Retailer. """
    products = ProductsSerializer(many=True)
    contacts = ContactsSerializer()
    provider = serializers.SerializerMethodField()

    class Meta:
        model = Retailer
        fields = ('id', 'name', 'contacts', 'provider', 'products', 'debt', 'created_at',)

    def update(self, obj, validated_data):
        """ Запрет на обновление через API поля «Задолженность». """
        validated_data.pop('debt', None)
        return super().update(obj, validated_data)

    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        return "Нет поставщика"


class TraderSerializer(BaseSerializer):
    products = ProductsSerializer(many=True)
    contacts = ContactsSerializer()
    provider = serializers.SerializerMethodField()

    class Meta:
        model = Trader
        fields = ('id', 'name', 'contacts', 'provider', 'products', 'debt', 'created_at',)

    def update(self, obj, validated_data):
        """ Запрет на обновление через API поля «Задолженность». """
        validated_data.pop('debt', None)
        return super().update(obj, validated_data)

    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        elif obj.provider_retailer:
            return obj.provider_retailer.name
        return "Нет поставщика"