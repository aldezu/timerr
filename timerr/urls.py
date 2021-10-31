from django.contrib import admin
from django.urls import include, path
from timerr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showForm)
]