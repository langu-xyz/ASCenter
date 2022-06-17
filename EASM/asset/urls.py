from django.urls import path, re_path, include
from rest_framework import routers
from . import views

app_name = "asset"

router = routers.DefaultRouter()
router.register(r'targetgroup', views.TargetGroupViewSet)
router.register(r'assetgroup', views.AssetGroupViewSet)
router.register(r'assetsubdomain', views.AssetSubdomainViewSet)
router.register(r'assetport', views.AssetPortViewSet)
router.register(r'asseturl', views.AssetUrlViewSet)
router.register(r'attacksurface', views.AttackSurfaceViewSet)

urlpatterns = [
    path(r'api/', include(router.urls))
]