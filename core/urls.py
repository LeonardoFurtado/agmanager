from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProjectViewSet, CustomerProjectsViewSet
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'projects', ProjectViewSet, basename='project')
customers_router = NestedSimpleRouter(router, r'customers', lookup='customer')
customers_router.register(r'projects', CustomerProjectsViewSet, basename='customer-projects')

urlpatterns = [
]
