from django.conf.urls import url, include
from rest_framework import routers
from BangazonAPI import views

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'paymenttypes', views.PaymentTypeViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderproduct', views.OrderProductViewSet)
router.register(r'trainingcourse', views.TrainingCourseViewSet)
router.register(r'department', views.DepartmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
