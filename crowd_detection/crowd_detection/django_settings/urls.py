
from django.contrib import admin
from django.urls import path, include
from crowd_detection import urls as crowd_detection_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(crowd_detection_urls)),

]
