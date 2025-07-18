from rest_framework.routers import DefaultRouter
from .views import UserDashboardViewSet

router = DefaultRouter()
router.register(r'dashboards', UserDashboardViewSet)

urlpatterns = router.urls
