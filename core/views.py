import logging

from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ModelViewSet
from core.models import Customer, Project, Activity
from core.serializers import CustomerSerializer, ProjectSerializer, ActivitySerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_pk')
        status = self.request.query_params.get('status')
        if customer_id:
            try:
                customer = Customer.objects.get(pk=customer_id)
            except Customer.DoesNotExist:
                raise NotFound('Customer not found.')
            queryset = Project.objects.filter(customer=customer).prefetch_related('activities')
            if status:
                queryset = queryset.filter(status=status).prefetch_related('activities')
            return queryset

        queryset = Project.objects.all().prefetch_related('activities')
        if status:
            queryset = queryset.filter(status=status).prefetch_related('activities')
        return queryset


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_pk')
        project_id = self.kwargs.get('project_pk')

        if customer_id:
            try:
                customer = Customer.objects.get(pk=customer_id)
            except Customer.DoesNotExist:
                raise NotFound(detail="Customer not found.")
            try:
                project = Project.objects.get(pk=project_id, customer=customer)
            except Project.DoesNotExist:
                raise NotFound(detail="Project not found for the given customer.")
        else:
            try:
                project = Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                raise NotFound(detail="Project not found.")

        return Activity.objects.filter(project=project)

    def perform_create(self, serializer):
        customer_id = self.request.data.get('customer')
        project_id = self.request.data.get('project')

        # not using try catch here because django serializer already did the validation if both customer and project exists.
        customer = Customer.objects.get(pk=customer_id)
        try:
            project = Project.objects.get(pk=project_id, customer=customer)
        except Project.DoesNotExist:
            raise NotFound(detail="Project not found for the given customer.")

        serializer.save(project=project)
