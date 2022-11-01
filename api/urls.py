from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('v1/', include("api.v1.urls")),
]

urlpatterns += [
    # YOUR PATTERNS
    path('v1/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('v1/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]