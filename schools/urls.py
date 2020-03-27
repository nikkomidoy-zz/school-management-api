from rest_framework_extensions.routers import ExtendedDefaultRouter

from schools.views import SchoolViewSet
from students.views import StudentViewSet

router = ExtendedDefaultRouter()

school_router = router.register('', SchoolViewSet, basename='schools')
school_router.register(
    'students',
    StudentViewSet,
    basename='schools-students',
    parents_query_lookups=['school',]
)

urlpatterns = router.urls
