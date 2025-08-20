# Issue Tracker REST API

A minimalist Issue Tracker REST API built with Django and Django REST Framework.

## Features

- Full CRUD operations for issues
- RESTful API endpoints with proper HTTP methods
- Issue status filtering (open, in_progress, closed)
- Session authentication for browsable API
- Custom browsable API template
- SQLite database for easy setup
- Comprehensive validation

## Technology Stack

- Python 3.7 (recommended)
- Django 3.2.25
- Django REST Framework 3.15.1
- SQLite database

## Project Structure

```
issue_tracker/
├── manage.py
├── requirements.txt
├── issue_tracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── issues/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    └── templates/
        └── rest_framework/
            └── api.html
```

## Installation & Setup

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Home page: http://127.0.0.1:8000/
   - API Browser: http://127.0.0.1:8000/api/
   - Admin interface: http://127.0.0.1:8000/admin/

## API Endpoints

### Issue Model
```json
{
    "id": 1,
    "title": "Issue title (max 140 chars)",
    "description": "Issue description",
    "status": "open|in_progress|closed", 
    "created_at": "2024-01-01T12:00:00Z",
    "updated_at": "2024-01-01T12:30:00Z"
}
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/issues/` | Create a new issue |
| GET | `/api/issues/` | List all issues |
| GET | `/api/issues/?status=open` | Filter issues by status |
| GET | `/api/issues/<int:id>/` | Retrieve specific issue |
| PATCH | `/api/issues/<int:id>/` | Update issue (title, description, status) |
| DELETE | `/api/issues/<int:id>/` | Delete issue |

### Example Usage

**Create an issue:**
```bash
curl -X POST http://127.0.0.1:8000/api/issues/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Fix login bug", "description": "Users cannot login", "status": "open"}'
```

**List all issues:**
```bash
curl http://127.0.0.1:8000/api/issues/
```

**Filter by status:**
```bash
curl http://127.0.0.1:8000/api/issues/?status=open
```

**Update an issue:**
```bash
curl -X PATCH http://127.0.0.1:8000/api/issues/1/ \
  -H "Content-Type: application/json" \
  -d '{"status": "closed"}'
```

## Authentication

- Session authentication is enabled for the browsable API
- No authentication required for API endpoints in development
- CSRF protection is configured for trusted origins

## Validation Rules

- **Title**: Required, maximum 140 characters
- **Status**: Must be one of: `open`, `in_progress`, `closed`
- **Description**: Optional, unlimited text

## Testing

Run the test suite:
```bash
python manage.py test
```

## Python Version Compatibility Note

This project is designed for Python 3.7 with Django 3.2.25. If you're using Python 3.12+ and encounter module import errors (like `ModuleNotFoundError: No module named 'cgi'`), you may need to:

1. Use Python 3.7-3.11 for full compatibility
2. Or upgrade Django to a newer version that supports your Python version

## Development Features

- Django admin interface for manual issue management  
- Browsable API with custom template and styling
- Comprehensive test coverage
- Proper HTTP status codes and error handling
- Clean URL patterns with regex support