from rest_framework import serializers
from .models import TargetGroup, AssetGroup, AssetSubdomain, AssetPort, AssetUrl, AttackSurface


class TargetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetGroup
        fields = '__all__'


class AssetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = '__all__'


class AssetSubdomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSubdomain
        fields = '__all__'


class AssetPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetPort
        fields = '__all__'


class AssetUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetUrl
        fields = '__all__'


class AttackSurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackSurface
        fields = '__all__'


