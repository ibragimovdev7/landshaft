from rest_framework import routers
from service import views

router = routers.DefaultRouter()
router.register(r'service',views.Serviceview,basename='service')