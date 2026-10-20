# NovaTech Labs — Agency API & Lead Engine (Backend)

High-performance REST API and administrative platform built with **Django 6.1.2** and **Django REST Framework 3.18.3** running on **Python 3.14.7**.

## 🌟 Capabilities
- **Case Study & Project API**: `GET /api/projects/` (supports `?category=` and `?featured=`) and `GET /api/projects/<slug>/`.
- **Services API**: `GET /api/services/`.
- **Testimonials API**: `GET /api/testimonials/`.
- **Inquiry & Lead Capture API**: `POST /api/inquiries/` with input validation and lead status tracking.
- **Real-Time Agency Stats API**: `GET /api/stats/`.
- **Django Admin Console**: Complete management of portfolio items, client leads, and reviews.

## 🛠️ Stack & Dependencies
- `Python`: `3.14.7`
- `Django`: `6.1.2`
- `djangorestframework`: `3.18.3`
- `django-cors-headers`: `4.9.0`

## 🚀 Getting Started

```powershell
# Create & activate virtual environment (using uv or standard python)
uv venv --python 3.14 .venv
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Run migrations & seed data
python manage.py migrate
python manage.py seed_data

# Run test suite
python manage.py test api

# Start development server
python manage.py runserver 127.0.0.1:8001
```
