from .models import Settings
from django.views.decorators.cache import cache_page
from django.core.cache import cache



def get_settings(request):


    #check if data in cache
    try:
        settings_data = cache.get('settings_data')
        print('cache')
    except Exception:
        print('data')
        settings_data = Settings.objects.last()
        cache.set('settings_data',settings_data,60*60*24)
    



    return {'settings_data': settings_data}

