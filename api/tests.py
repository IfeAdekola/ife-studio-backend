from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project, Service, Testimonial, Inquiry

class AgencyAPITests(APITestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            title="Test SaaS",
            slug="test-saas",
            subtitle="Subtitle 1",
            category="saas",
            category_label="SaaS Platform",
            description="A test saas app",
            impact_metrics="+100% Growth",
            tech_stack=["React", "Django"],
            features=["Auth", "Billing"],
            featured=True,
            order=1
        )
        self.project2 = Project.objects.create(
            title="Test E-commerce",
            slug="test-ecommerce",
            subtitle="Subtitle 2",
            category="ecommerce",
            category_label="E-Commerce",
            description="A test store",
            impact_metrics="+50% Sales",
            tech_stack=["React", "Stripe"],
            features=["Cart", "Checkout"],
            featured=False,
            order=2
        )
        self.service = Service.objects.create(
            title="Web Development",
            icon="Layers",
            tagline="Custom apps",
            description="We build web apps",
            deliverables=["Design", "Code"],
            timeline="3 Weeks"
        )
        self.testimonial = Testimonial.objects.create(
            client_name="Alice Smith",
            client_role="CEO",
            company="Alpha Corp",
            quote="Incredible work!",
            rating=5
        )

    def test_get_projects_list(self):
        response = self.client.get(reverse('project-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_projects_by_category(self):
        response = self.client.get(reverse('project-list') + '?category=saas')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['slug'], 'test-saas')

    def test_get_project_detail(self):
        response = self.client.get(reverse('project-detail', kwargs={'slug': 'test-saas'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test SaaS')

    def test_get_services_list(self):
        response = self.client.get(reverse('service-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Web Development')

    def test_get_testimonials_list(self):
        response = self.client.get(reverse('testimonial-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['client_name'], 'Alice Smith')

    def test_create_inquiry_success(self):
        data = {
            "name": "Bob Stone",
            "email": "bob@example.com",
            "company": "Stone Media",
            "project_type": "SaaS Platform",
            "budget_range": "$10,000 - $25,000",
            "timeline": "1-2 Months",
            "message": "We need a dashboard with auth and analytics.",
            "selected_features": ["User Authentication", "Dashboard"]
        }
        response = self.client.post(reverse('inquiry-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])
        self.assertEqual(Inquiry.objects.count(), 1)
        inquiry = Inquiry.objects.first()
        self.assertEqual(inquiry.name, "Bob Stone")
        self.assertEqual(inquiry.email, "bob@example.com")

    def test_create_inquiry_invalid_email(self):
        data = {
            "name": "Bob Stone",
            "email": "not-an-email",
            "message": "Hello"
        }
        response = self.client.post(reverse('inquiry-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_stats(self):
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('client_satisfaction', response.data)
        self.assertIn('uptime_reliability', response.data)
