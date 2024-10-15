from rest_framework import serializers
from chain.models import Contacts, Products, Factory, Retailer, Trader


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'email', 'country', 'city', 'street', 'office',)


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'model', 'release_date',)


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ('id', 'name', 'contacts', 'products', 'created_at',)


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        exclude = ('updated_at',)


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        exclude = ('updated_at',)
