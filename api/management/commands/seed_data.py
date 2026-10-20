from django.core.management.base import BaseCommand
from api.models import Project, Service, Testimonial, Inquiry

class Command(BaseCommand):
    help = 'Seeds database with realistic case studies, services, testimonials, and sample metrics'

    def handle(self, *args, **options):
        self.stdout.write("Clearing previous sample data...")
        Project.objects.all().delete()
        Service.objects.all().delete()
        Testimonial.objects.all().delete()
        Inquiry.objects.all().delete()

        self.stdout.write("Seeding showcase projects...")
        projects_data = [
            {
                "title": "FinPulse AI Analytics",
                "slug": "finpulse-ai-analytics",
                "subtitle": "Real-time algorithmic financial dashboard with predictive forecasting and sub-50ms latency.",
                "category": "saas",
                "category_label": "SaaS Platform",
                "description": "Engineered a high-throughput financial analysis platform handling 1.2M market ticks per second. Features interactive WebGL candlestick charts, automated anomaly detection, and end-to-end encrypted portfolio exports.",
                "impact_metrics": "+340% User Growth • 45ms P99 Latency • $18M Volume",
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://finpulse-demo.web.app",
                "github_url": "https://github.com/example/finpulse-core",
                "tech_stack": ["React 19", "Tailwind CSS", "Django REST", "PostgreSQL", "WebSockets", "Docker"],
                "features": [
                    "High-frequency live data streaming via WebSockets",
                    "Predictive trend modeling with Python statistical engines",
                    "Customizable multi-panel dashboard layouts with drag-and-drop",
                    "Role-based institutional access control & audit trails"
                ],
                "architecture_notes": "Decoupled React micro-frontend communicating with Django REST APIs and Redis-backed WebSocket streams.",
                "featured": True,
                "order": 1
            },
            {
                "title": "ShopFlow Headless Commerce",
                "slug": "shopflow-headless-commerce",
                "subtitle": "Ultra-fast headless shopping platform with instant search, multi-currency checkout, and 99 PageSpeed.",
                "category": "ecommerce",
                "category_label": "E-Commerce Solution",
                "description": "Developed a next-generation luxury retail storefront powered by edge caching, dynamic inventory reconciliation, and frictionless one-click Stripe payments.",
                "impact_metrics": "+62% Checkout Conversion • 0.4s Page Load • 4.9/5 Rating",
                "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://shopflow-storefront.web.app",
                "github_url": "https://github.com/example/shopflow-commerce",
                "tech_stack": ["React", "Tailwind CSS", "Django", "Stripe API", "Redis", "Cloudflare"],
                "features": [
                    "Instant typeahead search with fuzzy filtering",
                    "Dynamic cart drawer with optimistic UI updates",
                    "Stripe Checkout & Apple Pay / Google Pay integrations",
                    "Automated abandoned-cart recovery pipeline"
                ],
                "architecture_notes": "Server-side caching layer reduces database hits by 82% during traffic spikes.",
                "featured": True,
                "order": 2
            },
            {
                "title": "CloudScale DevOps Orchestrator",
                "slug": "cloudscale-devops-orchestrator",
                "subtitle": "Unified multi-cloud resource monitoring and auto-healing infrastructure management console.",
                "category": "fullstack",
                "category_label": "Full-Stack Web App",
                "description": "Architected an enterprise DevOps management console that visualizes Kubernetes clusters, automatically flags memory leaks, and orchestrates zero-downtime blue/green deployments.",
                "impact_metrics": "99.99% Guaranteed SLA • 4x Faster Rollbacks • 50+ Clouds",
                "image_url": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://cloudscale-console.web.app",
                "github_url": "https://github.com/example/cloudscale-orchestrator",
                "tech_stack": ["React", "Django REST", "Docker", "Kubernetes", "PostgreSQL", "Prometheus"],
                "features": [
                    "Visual topology tree of interconnected microservices",
                    "Automated canary deployment rollout controllers",
                    "Real-time cluster telemetry and threshold alerting",
                    "Granular IAM permissions and SAML 2.0 single sign-on"
                ],
                "architecture_notes": "Event-driven architecture with Celery workers processing health probes asynchronously.",
                "featured": True,
                "order": 3
            },
            {
                "title": "NexusAI Content Studio",
                "slug": "nexusai-content-studio",
                "subtitle": "Generative AI writing, localization, and brand tone refinement workstation for enterprise teams.",
                "category": "ai",
                "category_label": "AI-Powered Application",
                "description": "Built an interactive web studio that empowers marketing teams to generate, refine, and translate omnichannel brand copy while enforcing style guidelines and compliance checking.",
                "impact_metrics": "10x Content Output • 38 Languages • 12,000 Monthly Users",
                "image_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://nexusai-studio.web.app",
                "github_url": "https://github.com/example/nexusai-studio",
                "tech_stack": ["React 19", "Tailwind CSS", "Django", "OpenAI / Claude API", "PostgreSQL"],
                "features": [
                    "Token-by-token streaming markdown rendering",
                    "Side-by-side version comparison and diff editor",
                    "Custom tone-of-voice fine-tuning vectors",
                    "Export to CMS pipelines (WordPress, Contentful, Ghost)"
                ],
                "architecture_notes": "Stream processing responses with HTTP Server-Sent Events (SSE) directly from Django.",
                "featured": False,
                "order": 4
            },
            {
                "title": "Vitalis Telehealth Suite",
                "slug": "vitalis-telehealth-suite",
                "subtitle": "HIPAA-compliant patient booking, video consultations, and electronic health records web portal.",
                "category": "fullstack",
                "category_label": "Full-Stack Web App",
                "description": "Delivered a patient-friendly healthcare platform connecting licensed clinicians with over 20,000 patients across 12 countries. Engineered for zero data leaks and instantaneous video handshakes.",
                "impact_metrics": "20K+ Consultations • 0 Security Incidents • 99.8% CSAT",
                "image_url": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://vitalis-health.web.app",
                "github_url": "https://github.com/example/vitalis-health",
                "tech_stack": ["React", "Django REST", "WebRTC", "PostgreSQL", "AWS S3"],
                "features": [
                    "One-click encrypted WebRTC video calling",
                    "Integrated calendar scheduling and time-zone normalizer",
                    "EHR prescription generation with digital cryptographic signing",
                    "Multi-tier patient privacy and role isolation"
                ],
                "architecture_notes": "Compliant with strict HIPAA guidelines, zero client-side caching of PHI data.",
                "featured": False,
                "order": 5
            },
            {
                "title": "AeroSaaS Growth Engine",
                "slug": "aerosaas-growth-engine",
                "subtitle": "Conversion-optimized landing experience with interactive product tours and A/B test splitters.",
                "category": "landing",
                "category_label": "High-Converting Landing Page",
                "description": "Crafted a bespoke, lightning-fast product landing site featuring 3D glassmorphic elements, interactive ROI calculators, and friction-free social proof carousels.",
                "impact_metrics": "14.8% Visitor-to-Lead Rate • 100/100 Lighthouse • <400ms TTFB",
                "image_url": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=1200&q=80",
                "demo_url": "https://aerosaas-demo.web.app",
                "github_url": "https://github.com/example/aerosaas-lander",
                "tech_stack": ["React", "Tailwind CSS", "Framer Motion", "Django API"],
                "features": [
                    "Adaptive dark/light theme with contrast safety",
                    "Interactive ROI and payback timeline calculator",
                    "Dynamic lead capture modal with zero reload friction",
                    "Lightweight SVG vector graphics and optimized webp assets"
                ],
                "architecture_notes": "Strict performance budgets keeping total bundle size under 85KB gzipped.",
                "featured": False,
                "order": 6
            }
        ]

        for p_data in projects_data:
            Project.objects.create(**p_data)
        self.stdout.write(f"Created {len(projects_data)} projects.")

        self.stdout.write("Seeding agency services...")
        services_data = [
            {
                "title": "Custom Web Applications",
                "icon": "Layers",
                "tagline": "End-to-end engineering of production-ready web apps tailored to your business model.",
                "description": "From complex internal dashboards to customer-facing web applications, we design and build scalable, secure, and maintainable systems using React, Django, and modern cloud patterns.",
                "deliverables": [
                    "Full-Stack Architecture & System Design",
                    "Clean RESTful or GraphQL API Development",
                    "Modern Reactive UI with Tailwind CSS",
                    "Automated Unit & Integration Test Suites",
                    "CI/CD Deployment Pipelines"
                ],
                "timeline": "3 to 6 Weeks",
                "order": 1
            },
            {
                "title": "SaaS Platform & MVP Launch",
                "icon": "Zap",
                "tagline": "Turn product ideas into validated, scalable software platforms in record time.",
                "description": "We specialize in rapid MVP execution without cutting corners on software hygiene. We deliver fully functioning user auth, subscription billing, multi-tenant databases, and analytics.",
                "deliverables": [
                    "Multi-Tenant Database Architecture",
                    "Stripe Billing & Tiered Subscription Engine",
                    "User Authentication (OAuth, JWT, 2FA)",
                    "Customer Onboarding Workflows",
                    "Production Cloud Infrastructure"
                ],
                "timeline": "4 to 8 Weeks",
                "order": 2
            },
            {
                "title": "High-Converting Landing Pages",
                "icon": "Globe",
                "tagline": "Pixel-perfect, ultra-fast landing experiences that turn clicks into paying customers.",
                "description": "We blend design psychology, interactive calculators, micro-interactions, and 100/100 Core Web Vitals to deliver landing experiences that outperform industry conversion benchmarks.",
                "deliverables": [
                    "Conversion-Rate-Optimized (CRO) UX/UI",
                    "Interactive Feature Demos & Calculators",
                    "Lighthouse 95+ Core Web Vitals Score",
                    "Full Mobile & Tablet Responsive Layouts",
                    "Lead Capture CRM Integration"
                ],
                "timeline": "1 to 2 Weeks",
                "order": 3
            },
            {
                "title": "API Engineering & Cloud Systems",
                "icon": "Cpu",
                "tagline": "Robust backend APIs, database optimization, and cloud orchestration that never flinches under load.",
                "description": "We build rock-solid backend services in Django and Python that integrate smoothly with third-party APIs, process background queues, and scale effortlessly.",
                "deliverables": [
                    "REST / GraphQL High-Performance APIs",
                    "PostgreSQL Schema Design & Query Optimization",
                    "Redis Caching & Asynchronous Task Queues",
                    "Docker Containerization & Cloud Deployment",
                    "Comprehensive API Swagger / OpenAPI Docs"
                ],
                "timeline": "2 to 4 Weeks",
                "order": 4
            }
        ]

        for s_data in services_data:
            Service.objects.create(**s_data)
        self.stdout.write(f"Created {len(services_data)} services.")

        self.stdout.write("Seeding client testimonials...")
        testimonials_data = [
            {
                "client_name": "Marcus Vance",
                "client_role": "CTO & Co-Founder",
                "company": "QuantPulse Capital",
                "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80",
                "quote": "The team took our complex financial models and built an intuitive, blisteringly fast web app in just 5 weeks. Our institutional clients routinely praise how responsive the platform is.",
                "rating": 5,
                "project_name": "FinPulse AI Analytics",
                "featured": True
            },
            {
                "client_name": "Elena Rostova",
                "client_role": "Head of Digital Commerce",
                "company": "Vanguard Retail Group",
                "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=200&q=80",
                "quote": "Our previous checkout experience was clunky and slow. The redesigned headless store increased our conversion rate by 62% in the very first month post-launch. Exceptional execution.",
                "rating": 5,
                "project_name": "ShopFlow Headless Commerce",
                "featured": True
            },
            {
                "client_name": "David Chen",
                "client_role": "VP of Engineering",
                "company": "Skyline HealthTech",
                "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=80",
                "quote": "Finding developers who understand modern React, clean Python backend architecture, and strict security compliance is rare. They delivered on every single promise ahead of schedule.",
                "rating": 5,
                "project_name": "Vitalis Telehealth Suite",
                "featured": True
            }
        ]

        for t_data in testimonials_data:
            Testimonial.objects.create(**t_data)
        self.stdout.write(f"Created {len(testimonials_data)} testimonials.")

        self.stdout.write("Seeding sample client inquiry...")
        Inquiry.objects.create(
            name="Sarah Jenkins",
            email="sarah.jenkins@acme-ventures.com",
            company="Acme Ventures",
            project_type="SaaS Platform MVP",
            budget_range="$10k - $25k",
            timeline="1-2 Months",
            message="Looking to build a client-facing venture portal with role-based access, document upload, and automated financial reporting.",
            selected_features=["User Authentication", "Subscription Billing", "Admin Dashboard", "AI Integration"],
            status="contacted"
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded all showcase data!"))
