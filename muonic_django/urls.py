from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'runs', views.RunViewSet)
router.register(r'analyzers', views.AnalyzerViewSet)
router.register(r'velocities', views.VelocityViewSet)
router.register(r'rates', views.RateViewSet)
router.register(r'decays', views.DecayViewSet)
router.register(r'pulses', views.PulseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]