from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Service, Testimonial, Inquiry
from .serializers import (
    ProjectSerializer,
    ServiceSerializer,
    TestimonialSerializer,
    InquirySerializer
)

class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)

        if category and category != 'all':
            queryset = queryset.filter(category=category)
        if featured is not None:
            queryset = queryset.filter(featured=featured.lower() == 'true')

        return queryset


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class InquiryCreateView(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "success": True,
                "message": "Thank you! Your project inquiry has been received. Our team will contact you within 24 hours.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class StatsView(APIView):
    def get(self, request):
        total_projects = Project.objects.count()
        total_testimonials = Testimonial.objects.count()
        total_inquiries = Inquiry.objects.count()

        stats = {
            "projects_completed": total_projects if total_projects > 0 else 24,
            "client_satisfaction": "99.4%",
            "average_lcp_speed": "<650ms",
            "uptime_reliability": "99.99%",
            "production_deployments": 140,
            "inquiries_processed": total_inquiries
        }
        return Response(stats)
