from django.contrib import admin
from django.urls import path
from core.views import testing_view, testing_detail_view, health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing', testing_view, name='testing'),
    path('testing/<int:id>', testing_detail_view, name='testing-detail'),
    path('health', health_check, name='health'),
]