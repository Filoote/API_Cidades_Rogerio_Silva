from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cidade.views import EstadoViewSet, CidadeViewSet
from usuarios.views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(openapi.Info(title="API Cidades", default_version='v1'), public=True)

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cidade.urls')),  # Corrija para string: 'cidade.urls'
    path('api/signup/', SignupView.as_view()),
    path('api/signin/', TokenObtainPairView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
