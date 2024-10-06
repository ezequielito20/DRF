from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def validate_measure_unit(self, value):
        if value == '' or value is None:
            raise serializers.ValidationError('Unit measure is required')
        return value
    
    def validate_category_product(self, value):
        if value == '' or value is None:
            raise serializers.ValidationError('Category product is required')
        return value
    
    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({'measure_unit' : 'Unit measure is required'})
        
        if 'category_product' not in data.keys():
            raise serializers.ValidationError({ 'category_product' : 'Category product is required'})
        return data
    
    # forma correcta
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit else '', 
            'category_product': instance.category_product.description if instance.category_product else '',
            
        }
        