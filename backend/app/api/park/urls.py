from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FeedbackViewSet, ParkViewSet

router = DefaultRouter()
router.register("park", ParkViewSet, basename="park")
router.register("feedback", FeedbackViewSet, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
]
