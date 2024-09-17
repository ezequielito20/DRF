from rest_framework import viewsets

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(state=True)

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    queryset = IndicatorSerializer.Meta.model.objects.filter(state=True)

class CategoryProductSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.filter(state=True)

