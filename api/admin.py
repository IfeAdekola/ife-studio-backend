from django.contrib import admin
from .models import Project, Service, Testimonial, Inquiry

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'order', 'created_at')
    list_filter = ('category', 'featured', 'created_at')
    search_fields = ('title', 'subtitle', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', '-created_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'timeline', 'order')
    search_fields = ('title', 'tagline', 'description')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'featured')
    list_filter = ('rating', 'featured')
    search_fields = ('client_name', 'company', 'quote')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'project_type', 'budget_range', 'status', 'created_at')
    list_filter = ('status', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
