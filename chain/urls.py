from django.urls import path
from chain.views import (
    ContactsViewSet,
    ProductsViewSet,
    RetailerViewSet,
    TraderViewSet,
    FactoryListAPIView,
    FactoryViewSet

)
from chain.apps import ChainConfig
from rest_framework.routers import DefaultRouter

app_name = ChainConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contacts')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'factories', FactoryViewSet, basename='factories')
router.register(r'retailers', RetailerViewSet, basename='retailers')
router.register(r'traders', TraderViewSet, basename='traders')


urlpatterns = [
    path('factories/list', FactoryListAPIView.as_view(), name='factories_list'),
]+router.urls