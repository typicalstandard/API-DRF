from rest_framework import serializers
from .models import Link,Collection

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'description', 'url', 'image', 'link_type', 'created_at', 'updated_at', 'user']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user']
