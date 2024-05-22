import logging

from rest_framework.viewsets import ModelViewSet

from core.models import Customer, Project, Activity
from core.serializers import CustomerSerializer, ProjectSerializer, ActivitySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CustomerProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_pk']
        return Project.objects.filter(customer_id=customer_id)


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        project_id = self.kwargs['project_pk']
        return Activity.objects.filter(project_id=project_id)
