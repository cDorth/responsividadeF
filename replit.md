# MySphere - Professional Social Network Platform

## Project Overview
MySphere is a Django-based multi-tenant professional social network platform imported from GitHub. It allows organizations to create their own isolated social networks with features for posting, messaging, events, gamification, and more.

## Current Status
The application is fully configured and running on Replit with:
- Django 5.2.6 on Python 3.11
- SQLite database (development)
- Complete mobile responsive design
- Bottom navigation menu for mobile devices
- All core features functional

## Recent Changes (November 21, 2025)

### Environment Setup
- Installed Python 3.11 module
- Configured environment variables (SECRET_KEY, FERNET_KEY, DEBUG=True)
- Modified settings.py for Replit compatibility
- Set up in-memory channels layer for WebSockets
- Configured workflow to run on port 5000

### Mobile Responsive Design
- Added comprehensive CSS media queries for mobile devices
- Hid sidebar panels (left and right) on screens < 1024px
- Created bottom navigation menu for mobile with icons for:
  - Feed
  - Profile
  - Gamificação
  - Conquistas
  - Eventos
  - Chat
- Maintained all existing functionality while improving mobile UX
- Responsive breakpoints at 1024px (tablet), 640px (phone), and 380px (small phone)
- All sidebar menu items accessible through bottom navigation on mobile

### Database
- Using SQLite for development (db.sqlite3)
- All migrations applied successfully
- Multi-tenant architecture with tenant isolation

## Project Architecture

### Key Components
- **Multi-tenant System**: Each organization has isolated data
- **Authentication**: Django Allauth with custom user model
- **Feed**: Social media-style posts with likes, comments, shares
- **Chat**: Real-time messaging between users
- **Events**: Event management system
- **Gamification**: Point system and achievements
- **Staff Panel**: Administrative interface for staff users

### File Structure
```
MySphere/
├── MySphere/          # Project settings
├── accounts/          # User authentication and profiles
├── feed/              # Social feed and posts
├── chat/              # Messaging system
├── eventos/           # Events management
├── gamification/      # Gamification system
├── tenants/           # Multi-tenant management
├── media/             # User uploaded files
├── staticfiles/       # Collected static files
└── db.sqlite3         # SQLite database
```

## User Preferences

### Development Commands
- Always use `python3.11` explicitly for Django commands
- Use `unset DATABASE_URL &&` prefix when running manage.py commands
- This ensures compatibility with Replit environment

### Mobile-First Design
- Prioritize mobile experience with clean, minimalist UI
- Hide unnecessary elements on small screens
- Use bottom navigation for easy thumb access on mobile devices

## Running the Application

### Development Server
The Django development server is configured to run on `0.0.0.0:5000` to work with Replit's proxy system.

Workflow command:
```bash
unset DATABASE_URL && python3.11 manage.py runserver 0.0.0.0:5000
```

### Creating a Superuser
To create an admin account:
```bash
unset DATABASE_URL && python3.11 manage.py createsuperuser
```

### Collecting Static Files
After making CSS/JS changes:
```bash
unset DATABASE_URL && python3.11 manage.py collectstatic --noinput
```

## Dependencies
See `requirements.txt` for full list. Key dependencies:
- Django 5.2.6
- channels (WebSocket support)
- django-allauth (authentication)
- django-cryptography (encryption)
- Pillow (image processing)
- psycopg2-binary (PostgreSQL support)

## Features
1. **Social Feed**: Post text, images, videos, files with hashtags and mentions
2. **Real-time Chat**: Direct messaging with WebSocket support
3. **Events**: Create and manage events with RSVP
4. **Gamification**: Points, levels, and achievements system
5. **Multi-tenant**: Complete data isolation per organization
6. **Mobile Responsive**: Full mobile support with bottom navigation

## Known Issues & Notes
- PostgreSQL had compatibility issues with Python version conflicts, using SQLite as fallback
- Static files must be collected after CSS/JS changes
- Server must be running to see updates in the web preview
- Mobile view activates at screen width < 1024px

## Next Steps
- Consider migrating to PostgreSQL for production
- Add more interactive features to bottom navigation
- Optimize image loading for mobile devices
- Implement progressive web app (PWA) features
