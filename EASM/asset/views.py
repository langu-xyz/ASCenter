from django.shortcuts import render

# Create your views here.

from .models import TargetGroup, AssetGroup, AssetSubdomain, AssetPort, AssetUrl, AttackSurface
from rest_framework import viewsets
from .serializer import TargetGroupSerializer, AssetGroupSerializer, AssetSubdomainSerializer, AssetPortSerializer, AssetUrlSerializer, AttackSurfaceSerializer


class TargetGroupViewSet(viewsets.ModelViewSet):
    queryset = TargetGroup.objects.all()
    serializer_class = TargetGroupSerializer


class AssetGroupViewSet(viewsets.ModelViewSet):
    queryset = AssetGroup.objects.all()
    serializer_class = AssetGroupSerializer


class AssetSubdomainViewSet(viewsets.ModelViewSet):
    queryset = AssetSubdomain.objects.all()
    serializer_class = AssetSubdomainSerializer


class AssetPortViewSet(viewsets.ModelViewSet):
    queryset = AssetPort.objects.all()
    serializer_class = AssetPortSerializer


class AssetUrlViewSet(viewsets.ModelViewSet):
    queryset = AssetUrl.objects.all()
    serializer_class = AssetUrlSerializer


class AttackSurfaceViewSet(viewsets.ModelViewSet):
    queryset = AttackSurface.objects.all()
    serializer_class = AttackSurfaceSerializer
    