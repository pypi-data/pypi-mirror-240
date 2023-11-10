from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_rolesandgroups'

router = NetBoxRouter()
router.register('system-role', views.SystemRoleViewSet)
router.register('tech-role', views.TechRoleViewSet)

urlpatterns = router.urls
