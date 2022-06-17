from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.TargetGroup)
class TargetGroupView(admin.ModelAdmin):
    list_display = ('updated_time', 'name', 'domain')
    search_fields = ('name', 'domain')
    list_display_links = ("name",)
    list_per_page = 10


@admin.register(models.AssetGroup)
class AssetGroupView(admin.ModelAdmin):
    list_display = ('updated_time', 'domain_name', 'domain', 'target_name')
    search_fields = ('domain', 'target_name')
    list_display_links = ("domain",)
    list_per_page = 10


@admin.register(models.AssetSubdomain)
class AssetSubdomainView(admin.ModelAdmin):
    list_display = ('updated_time', 'subdomain', 'domain', 'ip', 'title', 'fingerprint', 'waf')
    search_fields = ('domain', 'subdomain')
    list_display_links = ("subdomain",)
    list_per_page = 10


@admin.register(models.AssetPort)
class AssetPortView(admin.ModelAdmin):
    list_display = ('updated_time', 'ip', 'port', 'service', 'service_info')
    search_fields = ('ip', 'service')
    list_display_links = ("ip",)
    list_per_page = 10


@admin.register(models.AssetUrl)
class AssetUrlView(admin.ModelAdmin):
    list_display = ('updated_time', 'api_name', 'uri', 'subdomain', 'post_data', 'request_data', 'response_data', 'iframe_fingerprint', 'params_json', 'ret_code', 'method', 'referer', 'cookie', 'res_info')
    search_fields = ('api_name', 'subdomain')
    list_display_links = ("api_name",)
    list_per_page = 10


@admin.register(models.AttackSurface)
class AttackSurfaceView(admin.ModelAdmin):
    list_display = ('updated_time', 'assert_name', 'vuln_name', 'vuln_level', 'poc_info')
    search_fields = ('assert_name', 'vuln_name', 'vuln_level')
    list_display_links = ("assert_name",)
    list_per_page = 10

