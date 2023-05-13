from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"hashtags", views.HashtagViewset, basename="hashtags")
router.register(r"projects", views.ProjectViewset, basename="projects")

urlpatterns = router.urls