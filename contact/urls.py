from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter

from .views import ContactUploadView, ContactView

router = DefaultRouter()
router.register('api/contact', ContactView, base_name='contact')

urlpatterns = [
    path('', include(router.urls)),
    path('api/csv_upload/',  csrf_exempt(ContactUploadView.as_view()))
]
