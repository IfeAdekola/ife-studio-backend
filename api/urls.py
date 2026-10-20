from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ServiceListView,
    TestimonialListView,
    InquiryCreateView,
    StatsView
)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('inquiries/', InquiryCreateView.as_view(), name='inquiry-create'),
    path('stats/', StatsView.as_view(), name='stats'),
]
