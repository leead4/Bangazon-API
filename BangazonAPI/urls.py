from django.conf.urls import url, include
from rest_framework import routers
from BangazonAPI.bangazon import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bangazon/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
