from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models import Customer, Activity, Project


class CustomerSerializer(serializers.ModelSerializer):
    # projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate_customer(self, value):
        if not value.active:
            raise ValidationError("The customer is not active.")
        return value
