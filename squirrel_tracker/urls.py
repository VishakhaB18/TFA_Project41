from django.contrib import admin
from django.urls import path, include
from tracking.views import map_view
from tracking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sightings/', include('tracking.urls')),
    path('stats', views.stats),
    path('add', views.add_sighting),
    path('map/', map_view),
    path('<str:pk>', views.update_or_delete)
]
