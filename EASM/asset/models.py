from django.db import models


# Create your models here.


class TargetGroup(models.Model):
    """
    name
    domain
    time
    desc
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    name = models.CharField(max_length=50, primary_key=True, verbose_name='Group Name')
    domain = models.CharField(max_length=100, verbose_name='Domain')
    desc = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "TargetGroup"
        verbose_name_plural = "TargetGroup"
        ordering = ['name']


class AssetGroup(models.Model):
    """
    domain_name
    domain
    target_name
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    domain_name = models.CharField(max_length=50, primary_key=True, verbose_name='Company Name')
    domain = models.CharField(max_length=100, verbose_name='Domain')
    target_name = models.CharField(max_length=50, verbose_name='Group Name')

    def __unicode__(self):
        return self.domain_name

    class Meta:
        verbose_name = "AssetGroup"
        verbose_name_plural = "AssetGroup"
        ordering = ['domain_name']


class AssetSubdomain(models.Model):
    """
    domain
    subdomain
    ip
    title
    fingerprint
    waf
    time
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    subdomain = models.CharField(max_length=100, primary_key=True, verbose_name="Subdomain")
    domain = models.CharField(max_length=100, verbose_name="Domain")
    ip = models.CharField(max_length=50, verbose_name="IP")
    title = models.CharField(max_length=200, verbose_name="Web Title")
    fingerprint = models.CharField(max_length=200, verbose_name="Web Fingerprint")
    waf = models.CharField(max_length=100, verbose_name="WAF Fingerprint")

    def __unicode__(self):
        return self.subdomain

    class Meta:
        verbose_name = "AssetSubdomain"
        verbose_name_plural = "AssetSubdomain"
        ordering = ['subdomain']



class AssetPort(models.Model):
    """
    ip
    port
    service
    version
    time
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    ip = models.CharField(max_length=50, verbose_name="IP")
    port = models.CharField(max_length=30, verbose_name="Port")
    service = models.CharField(max_length=200, verbose_name="Service")
    service_info = models.TextField(verbose_name="Service Info")

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = "AssetPort"
        verbose_name_plural = "AssetPort"
        ordering = ['ip']


class AssetUrl(models.Model):
    """
    api
    url
    subdomain
    post_data
    request_data
    response_data
    time
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    api_name = models.CharField(max_length=200, verbose_name="API Name")
    uri = models.CharField(max_length=500, verbose_name="URI")
    subdomain = models.CharField(max_length=200, verbose_name="HOST")
    post_data = models.CharField(max_length=1000, verbose_name="Post Data")
    request_data = models.TextField(verbose_name="Request Data Raw")
    response_data = models.TextField(verbose_name="Response Data Raw")
    iframe_fingerprint = models.CharField(max_length=200, verbose_name="Iframe")
    params_json = models.CharField(max_length=200, verbose_name="Params")
    ret_code = models.IntegerField(verbose_name="RetCode")
    method = models.CharField(max_length=50, verbose_name="Method")
    referer = models.CharField(max_length=200, verbose_name="Referer")
    cookie = models.CharField(max_length=500, verbose_name="Cookie")
    res_info = models.CharField(max_length=200, verbose_name="Response Info")

    def __unicode__(self):
        return self.api_name

    class Meta:
        verbose_name = "AssetUrl"
        verbose_name_plural = "AssetUrl"
        ordering = ['api_name']


class AttackSurface(models.Model):
    """
    assert_name
    vuln_name
    vuln_level: "1-High", "2-Medium", "3-Low", "4-Information" or "4-False positive"
    poc_info
    """
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Updated Time")
    assert_name = models.CharField(max_length=100, verbose_name="Assert Name")
    vuln_name = models.CharField(max_length=500, verbose_name="Vuln Name")
    vuln_level = models.IntegerField(verbose_name="Vuln Level")
    poc_info = models.TextField(verbose_name="Poc Info")

    def __unicode__(self):
        return self.assert_name

    class Meta:
        verbose_name = "AttackSurface"
        verbose_name_plural = "AttackSurface"
        ordering = ['assert_name']
