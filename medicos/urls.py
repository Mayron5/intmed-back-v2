from rest_framework.routers import SimpleRouter

from .views import MedicoViewSet

router = SimpleRouter()
router.register('', MedicoViewSet)