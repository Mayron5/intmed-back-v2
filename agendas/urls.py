from rest_framework.routers import SimpleRouter

from .views import AgendaViewSet

router = SimpleRouter()
router.register('', AgendaViewSet)