from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
)


router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet)
router.register(r'cart-view', views.CartListView, basename='cart_product_view')
router.register(r'user', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'register', views.RegisterViewSet, basename='register_user')

app_name = 'main'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('register/', views.RegisterAPIView.as_view(), name='register')
]
