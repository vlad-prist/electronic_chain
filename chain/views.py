from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from chain.models import Contacts, Products, Factory, Retailer, Trader
from chain.serializers import (
    ContactsSerializer,
    ProductsSerializer,
    FactorySerializer,
    RetailerSerializer,
    TraderSerializer,
)
from chain.filters import (
    FactoryCountryFilter,
    RetailerCountryFilter,
    TraderCountryFilter
)
from chain.paginators import CustomPagination


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        contacts = serializer.save()
        contacts.save()
        return contacts


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        products = serializer.save()
        products.save()
        return products


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        factory = serializer.save()
        factory.save()
        return factory


class FactoryListAPIView(generics.ListAPIView):
    """
    Запрашивает из БД список всех экземпляров модели Factory, отсортированных по названию.
    """
    queryset = Factory.objects.all().order_by("name")
    serializer_class = FactorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactoryCountryFilter
    pagination_class = CustomPagination


class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        retailer = serializer.save()
        retailer.save()
        return retailer


class RetailerListAPIView(generics.ListAPIView):
    """
    Запрашивает из БД список всех экземпляров модели Retailer, отсортированных по названию.
    """
    queryset = Retailer.objects.all().order_by("name")
    serializer_class = RetailerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RetailerCountryFilter
    pagination_class = CustomPagination


class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        trader = serializer.save()
        trader.save()
        return trader


class TraderListAPIView(generics.ListAPIView):
    """
    Запрашивает из БД список всех экземпляров модели Trader, отсортированных по названию.
    """
    queryset = Trader.objects.all().order_by("name")
    serializer_class = TraderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TraderCountryFilter
    pagination_class = CustomPagination
