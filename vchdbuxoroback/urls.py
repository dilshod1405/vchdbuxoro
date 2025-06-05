from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
from content.permissions import IsAdminUserOnly

swagger_view = SpectacularSwaggerView.as_view(
    permission_classes=[IsAdminUserOnly]
)

redoc_view = SpectacularRedocView.as_view(
    permission_classes=[IsAdminUserOnly]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include('content.urls')),
    path('rosetta/', include('rosetta.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), 
    path('api/redoc/', redoc_view, name='redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)