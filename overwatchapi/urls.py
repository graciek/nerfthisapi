from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from overwatchapi.api import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'voicelines', views.VoiceLineViewSet)
router.register(r'abilities', views.AbilityViewSet)
router.register(r'maps', views.MapViewSet)

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^docs/',
        views.Documentation.as_view(), name='documentation'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(
        r'^api/v1/',
        include(router.urls, namespace='apiv1')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
