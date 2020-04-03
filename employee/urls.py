from django.urls import path, include
from rest_framework import routers
from employee import views
from employee.apiviews import EmployeeDetail

router = routers.DefaultRouter()
router.register(r'type', views.EmployeeTypeViewSet, basename="type")
router.register(r'product', views.ProductViewSet, basename="product")

urlpatterns = [
    path('index', views.index, name='index'),
    path('', include(router.urls)),
    path('emp/', EmployeeDetail.as_view()),
    path('emp/<int:pk>/', EmployeeDetail.as_view()),
]