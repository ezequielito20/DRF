from rest_framework.routers import DefaultRouter

from apps.products.api.views.product_viewsets import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'product',ProductViewSet,  basename='product')
router.register(r'measure-unit',MeasureUnitViewSet,  basename='measure_unit')
router.register(r'indicators',IndicatorViewSet,  basename='indicators')
router.register(r'category-products',CategoryProductSerializerViewSet,  basename='category_products')



urlpatterns = router.urls
