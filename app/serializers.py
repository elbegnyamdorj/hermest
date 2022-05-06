from rest_framework import serializers 
from .models import *

 
class AllSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BestComputers
        fields = ('id',
                  'name',
                  'price',
                  'category',
                  'prod_url',
                  'image_link')