from django.contrib import admin
from django.urls import path, include

from medicos.urls import router as router_medico
from especialidades.urls import router as router_especialidade
from agendas.urls import router as router_agendas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicos/', include(router_medico.urls)),
    path('especialidades/', include(router_especialidade.urls)),
    path('agendas/', include(router_agendas.urls)),
]
