from django_filters import rest_framework as filters
from chain.models import Factory, Retailer, Trader


class BaseCountryFilter(filters.FilterSet):
    """ Базовый класс для фильтрации по стране. """
    exact_country = filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')

    class Meta:
        abstract = True
        fields = ['contacts__country']


class FactoryCountryFilter(BaseCountryFilter):
    """ Класс для фильтрации по стране для модели Factory. """
    class Meta(BaseCountryFilter.Meta):
        model = Factory


class RetailerCountryFilter(BaseCountryFilter):
    """ Класс для фильтрации по стране для модели Retailer. """
    class Meta(BaseCountryFilter.Meta):
        model = Retailer


class TraderCountryFilter(BaseCountryFilter):
    """ Класс для фильтрации по стране для модели Trader. """
    class Meta(BaseCountryFilter.Meta):
        model = Trader
