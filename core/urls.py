from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path,
)


urlpatterns = [
    path('api/v1/', include('core.api_urls')),
    path('', admin.site.urls),
]

title: str = 'Exchange Rate'
admin.site.site_header = title
admin.site.site_title = f'{title} Admin'
admin.site.index_title = f'Welcome to {title} Administration'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
