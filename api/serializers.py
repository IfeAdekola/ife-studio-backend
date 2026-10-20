from rest_framework import serializers
from .models import Project, Service, Testimonial, Inquiry

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'subtitle', 'category', 'category_label',
            'description', 'impact_metrics', 'image_url', 'demo_url', 'github_url',
            'tech_stack', 'features', 'architecture_notes', 'featured', 'order', 'created_at'
        ]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'icon', 'tagline', 'description', 'deliverables', 'timeline', 'order']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'client_name', 'client_role', 'company', 'avatar', 'quote', 'rating', 'project_name', 'featured']

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            'id', 'name', 'email', 'company', 'project_type',
            'budget_range', 'timeline', 'message', 'selected_features',
            'status', 'created_at'
        ]
        read_only_fields = ['id', 'status', 'created_at']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value.strip()

    def validate_email(self, value):
        if not value.strip():
            raise serializers.ValidationError("Email is required.")
        return value.strip().lower()
