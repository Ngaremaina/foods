from rest_framework.routers import DefaultRouter
from .views import UserViewSet,CategoryViewSet,ProductViewSet,SalesViewSet,PaymentViewSet,CustomerViewSet,CartViewSet,LocationViewSet,AdminViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'admins', AdminViewSet, basename='admin')

urlpatterns = router.urls

