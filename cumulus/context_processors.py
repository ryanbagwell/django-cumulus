from cumulus.settings import CUMULUS
from cumulus.storage import CloudFilesStorage


def cdn_url(request):
    """
    A context processor to expose the full cdn url in templates.

    """
    cloudfiles_storage = CloudFilesStorage()
    container_url = cloudfiles_storage._get_container_url()
    cdn_url = container_url + CUMULUS.get('STATIC_PREFIX', '')

    return {'CDN_URL': cdn_url}