from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book.views.book import BookViewSet

router = DefaultRouter()
router.register("", BookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls))
]
