from django.urls import path
from rest_framework.routers import DefaultRouter
from language.views import LanguageListView
router = DefaultRouter()
router.register(r'language', LanguageListView)
urlpatterns = urlpatterns = router.urls

