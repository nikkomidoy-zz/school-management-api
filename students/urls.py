from rest_framework_extensions.routers import ExtendedDefaultRouter

from students.views import StudentViewSet

router = ExtendedDefaultRouter()

router.register('', StudentViewSet, basename='students')

urlpatterns = router.urls
