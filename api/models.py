from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('saas', 'SaaS Platform'),
        ('fullstack', 'Full-Stack Web App'),
        ('ecommerce', 'E-Commerce Solution'),
        ('landing', 'High-Converting Landing Page'),
        ('ai', 'AI-Powered Application'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=300)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='fullstack')
    category_label = models.CharField(max_length=100, default='Full-Stack Web App')
    description = models.TextField()
    impact_metrics = models.CharField(max_length=200, help_text="e.g. +340% Conversions • <650ms Latency")
    image_url = models.CharField(max_length=500, blank=True)
    demo_url = models.CharField(max_length=500, default='#')
    github_url = models.CharField(max_length=500, default='#')
    tech_stack = models.JSONField(default=list, help_text="List of technologies used")
    features = models.JSONField(default=list, help_text="List of key features delivered")
    architecture_notes = models.TextField(blank=True, help_text="Architectural highlights or stack choices")
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.category})"


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, default='Layers', help_text="Lucide icon name")
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    deliverables = models.JSONField(default=list)
    timeline = models.CharField(max_length=100, default="2-4 Weeks")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    client_role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    avatar = models.CharField(max_length=500, blank=True)
    quote = models.TextField()
    rating = models.IntegerField(default=5)
    project_name = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.company}"


class Inquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Lead'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    project_type = models.CharField(max_length=100)
    budget_range = models.CharField(max_length=100)
    timeline = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    selected_features = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return f"Inquiry from {self.name} ({self.company or 'Direct'}) - {self.project_type}"
