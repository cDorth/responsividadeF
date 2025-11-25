# MySphere - Professional Social Network

## Overview
MySphere is a multi-tenant professional social network platform built with Django. It's designed for companies seeking innovation, competitiveness, and integration across different areas of the organization. The platform provides an interactive and customizable experience focused on real-time communication and integration.

## Purpose
A professional social network for businesses that provides:
- Real-time communication via WebSocket chat
- Gamification system with points, levels, and achievements
- Event management and participation tracking
- Social feed with posts, comments, and interactions
- Multi-tenant architecture for isolated company environments

## Current State
The application has been successfully configured for the Replit environment and is running. The development server is accessible via the webview, and all core features are functional.

## Recent Changes (November 25, 2025)
- **Environment Setup**: Configured Python 3.11 with all required dependencies
- **Database Configuration**: Set up SQLite as the default database (can be switched to PostgreSQL by setting DATABASE_URL)
- **Channel Layer**: Configured Django Channels with InMemoryChannelLayer for WebSocket support
- **Cache Control**: Added middleware to prevent caching issues in Replit's iframe proxy
- **Workflow**: Created Django development server workflow on port 5000
- **Deployment**: Configured Gunicorn for production deployment
- **Environment Variables**: Set up SECRET_KEY, FERNET_KEY, and DEBUG variables

## Project Architecture

### Technology Stack
- **Backend**: Django 5.2.6 (Python web framework)
- **Database**: SQLite (development), PostgreSQL supported (production)
- **WebSockets**: Django Channels 4.0.0 for real-time chat
- **Authentication**: Django Allauth with Google OAuth support
- **Encryption**: Django Cryptography with Fernet fields for secure data
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Production Server**: Gunicorn

### Key Applications
1. **accounts**: User authentication and profile management
2. **chat**: Real-time messaging with WebSocket support
3. **tenants**: Multi-tenant architecture for company isolation
4. **feed**: Social feed with posts, comments, hashtags
5. **gamification**: Points, tasks, achievements, and ranking system
6. **eventos**: Event creation and participation management
7. **staff**: Administrative dashboard and user management

### Database Schema
The application uses Django's ORM with migrations for:
- Custom User model with tenant association
- Multi-tenant isolation via Tenant model
- Chat and Message models with file support
- Post and Comment models with media attachments
- Gamification system (Points, Tasks, Conquistas)
- Event management

## Environment Variables

### Required Variables (Already Set)
- `SECRET_KEY`: Django secret key for cryptographic signing
- `FERNET_KEY`: Encryption key for sensitive field encryption
- `DEBUG`: Set to "True" for development

### Optional Variables
- `DATABASE_URL`: PostgreSQL connection string (if using PostgreSQL)
- `EMAIL_USER`: Gmail address for sending password reset emails
- `EMAIL_PASSWORD`: Gmail app password for SMTP authentication
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Individual PostgreSQL credentials

## Development Workflow

### Running the Application
The application runs automatically via the configured workflow:
- **Command**: `python manage.py runserver 0.0.0.0:5000`
- **Port**: 5000 (required for Replit webview)
- **Host**: 0.0.0.0 (allows external connections)

### Making Changes
1. Edit code in the respective app directories
2. Create/modify models in `models.py`
3. Generate migrations: `python manage.py makemigrations`
4. Apply migrations: `python manage.py migrate`
5. The development server auto-reloads on file changes

### Creating Users
To create a superuser for admin access:
```bash
python manage.py createsuperuser
```

The app also includes a custom management command:
```bash
python manage.py create_test_users
```

## Production Deployment

### Configuration
- **Deployment Type**: Autoscale (stateless web application)
- **Server**: Gunicorn WSGI server
- **Command**: `gunicorn --bind=0.0.0.0:5000 --reuse-port MySphere.wsgi:application`

### Before Deploying
1. Set `DEBUG=False` in environment variables
2. Configure PostgreSQL database and set `DATABASE_URL`
3. Set up email credentials for password reset functionality
4. Run `python manage.py collectstatic` to gather static files
5. Consider setting up Redis for production chat (update CHANNEL_LAYERS in settings.py)

## File Structure
```
MySphere/
├── MySphere/          # Main project settings
│   ├── settings.py   # Django configuration
│   ├── urls.py       # URL routing
│   ├── wsgi.py       # WSGI application
│   └── asgi.py       # ASGI application (WebSockets)
├── accounts/         # User authentication
├── chat/            # Real-time messaging
├── tenants/         # Multi-tenant management
├── feed/            # Social feed
├── gamification/    # Points and achievements
├── eventos/         # Event management
├── staff/           # Admin dashboard
├── media/           # Uploaded files (encrypted)
├── staticfiles/     # Collected static files
└── manage.py        # Django CLI

```

## Known Issues & Warnings
- Static files directory `/home/runner/workspace/MySphere/static` does not exist (non-critical)
- `ACCOUNT_AUTHENTICATION_METHOD` is deprecated in django-allauth (functionality works, update recommended)

## User Preferences
None documented yet.

## Next Steps
1. Create initial tenant and users for testing
2. Configure email settings for password reset
3. Consider upgrading to PostgreSQL for production
4. Set up Redis for production WebSocket support
5. Update django-allauth configuration to use new LOGIN_METHODS setting
