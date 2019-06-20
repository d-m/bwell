from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'establishments', views.EstablishmentList)
router.register(r'inspections', views.InspectionList)
urlpatterns = router.urls
