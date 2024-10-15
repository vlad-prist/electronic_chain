from rest_framework import viewsets, generics
from chain.models import Contacts, Products, Factory, Retailer, Trader
from chain.serializers import (
    ContactsSerializer,
    ProductsSerializer,
    FactorySerializer,
    RetailerSerializer,
    TraderSerializer,
)


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def perform_create(self, serializer):
        contacts = serializer.save()
        contacts.save()
        return contacts


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        products = serializer.save()
        products.save()
        return products


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

    def perform_create(self, serializer):
        factory = serializer.save()
        factory.save()
        return factory


class FactoryListAPIView(generics.ListAPIView):
    """ Запрашивает из БД список всех фабрик, отсортированных по названию. """
    queryset = Factory.objects.all().order_by("name")
    serializer_class = FactorySerializer


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

    def perform_create(self, serializer):
        retailer = serializer.save()
        retailer.save()
        return retailer


class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

    def perform_create(self, serializer):
        trader = serializer.save()
        trader.save()
        return trader
