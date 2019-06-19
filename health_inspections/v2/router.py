from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'establishments', views.Establishment)
router.register(r'inspections', views.Inspection)
urlpatterns = router.urls
