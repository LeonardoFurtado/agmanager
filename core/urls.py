from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProjectViewSet, ActivityViewSet
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'activities', ActivityViewSet, basename='activity')

customers_router = NestedSimpleRouter(router, r'customers', lookup='customer')
customers_router.register(r'projects', ProjectViewSet, basename='customer-projects')

projects_router = NestedSimpleRouter(customers_router, r'projects', lookup='project')
projects_router.register(r'activities', ActivityViewSet, basename='project-activities')

urlpatterns = [
]
