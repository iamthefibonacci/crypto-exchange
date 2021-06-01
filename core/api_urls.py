from django.urls import (
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('auth/', include('dj_rest_auth.urls')),
    path('docs/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('', include('crypto.urls', namespace='crypto')),
]
