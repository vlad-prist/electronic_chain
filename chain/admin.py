from django.contrib import admin
from django.core.checks import messages
from chain.models import Contacts, Products, Factory, Retailer, Trader


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('country', 'city')
    search_fields = ('email', 'country', 'city',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date',)
    list_filter = ('name', 'model', 'release_date',)
    search_fields = ('name', 'model', 'release_date',)


class CityFilter(admin.SimpleListFilter):
    """ Кастомный фильтр ддя отображения города в админке. """
    title = 'Город'
    parameter_name = 'contacts__city'

    def lookups(self, request, model_admin):
        # Возвращает список уникальных городов для фильтрации
        cities = set(Contacts.objects.values_list('city', flat=True))
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        # Фильтрует по выбранному городу
        if self.value():
            return queryset.filter(contacts__city=self.value())
        return queryset


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'created_at',)
    list_filter = ('name', 'created_at', CityFilter)
    search_fields = ('name',)
    actions = ['set_null']

    @admin.action(description='Очистка задолженности покупателей у выбранных объектов')
    def set_null(self, request, queryset):
        queryset.update(debt=None)
        self.message_user(request, "Задолженности успешно очищены.", messages.WARNING)


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'created_at', 'get_provider',)
    list_filter = ('name', 'created_at', CityFilter)
    search_fields = ('name',)
    actions = ['set_null']

    @admin.display(description="Поставщик")
    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        return "Нет поставщика"

    @admin.action(description='Очистка задолженности перед поставщиком у выбранных объектов')
    def set_null(self, request, queryset):
        queryset.update(debt=None)
        self.message_user(request, "Задолженности успешно очищены.", messages.WARNING)


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'created_at', 'get_provider',)
    list_filter = ('name', 'created_at', CityFilter)
    search_fields = ('name',)
    actions = ['set_null']

    @admin.display(description="Поставщик")
    def get_provider(self, obj):
        if obj.provider_factory:
            return obj.provider_factory.name
        elif obj.provider_retailer:
            return obj.provider_retailer.name
        return "Нет поставщика"

    @admin.action(description='Очистка задолженности перед поставщиком у выбранных объектов')
    def set_null(self, request, queryset):
        queryset.update(debt=None)
        self.message_user(request, "Задолженности успешно очищены.", messages.WARNING)
