from rest_framework.routers import SimpleRouter

from .views import EspecialidadeViewSet

router = SimpleRouter()
router.register('', EspecialidadeViewSet)