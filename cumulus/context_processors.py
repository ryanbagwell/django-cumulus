from django.conf import settings
from cumulus.settings import CUMULUS
from cumulus.storage import CloudFilesStorage, CloudFilesStaticStorage

def _get_container_urls(cloudfiles_storage):
    cdn_url = cloudfiles_storage._get_container_url()
    ssl_url = cloudfiles_storage.container.public_ssl_uri()
    
    return cdn_url, ssl_url

def cdn_url(request):
    """
    A context processor to expose the full CDN URL in templates.
    """
    cdn_url, ssl_url = _get_container_urls(CloudFilesStorage())
    static_prefix = CUMULUS.get('STATIC_PREFIX', '')

    return {'CDN_URL': cdn_url+static_prefix, 'CDN_SSL_URL': ssl_url+static_prefix}

def static_cdn_url(request):
    """
    A context processor to expose the full static CDN URL 
    as static URL in templates.
    """
    cdn_url, ssl_url = _get_container_urls(CloudFilesStaticStorage())
    static_url = settings.STATIC_URL
    static_prefix = CUMULUS.get('STATIC_PREFIX', '')

    return {'STATIC_URL': cdn_url+static_prefix, 'STATIC_SSL_URL': ssl_url+static_prefix, 'LOCAL_STATIC_URL': static_url}
