# MySphere - Professional Social Network Platform

## Project Overview
MySphere is a Django-based multi-tenant professional social network platform imported from GitHub. It allows organizations to create their own isolated social networks with features for posting, messaging, events, gamification, and more.

## Current Status
The application is fully configured and running on Replit with:
- Django 5.2.6 on Python 3.11
- PostgreSQL database (Replit's built-in database)
- Complete mobile responsive design
- Bottom navigation menu for mobile devices
- **NEW**: Professionally redesigned eventos (events) page
- All core features functional

## Recent Changes (November 21, 2025)

### PostgreSQL Database Migration
- Successfully migrated from SQLite to PostgreSQL using Replit's built-in database
- All 58 migrations applied successfully to PostgreSQL
- Created test tenant "MySphere Corp" with test data
- Test credentials: teste@mysphere.com / teste123
- 5 sample events created for testing

### Events Page Complete Redesign
- **NEW**: Completely redesigned eventos page with professional, modern UI
- Follows MySphere design system with gradient purple theme
- Features:
  - Beautiful card-based grid layout for events
  - Event cards with images, date badges, and creator info
  - Interactive modal popup for full event details
  - Elegant animations and hover effects
  - Sticky navigation and sidebars
  - "Próximos Eventos" sidebar widget
  - Empty state handling
  - Edit/Delete buttons for staff users (inline on cards)
- Full responsive design with breakpoints at:
  - 1200px: Hides right sidebar
  - 968px: Collapses to single column, hides left sidebar
  - 640px: Full mobile optimization
- New files:
  - eventos/templates/eventos/index.html (complete redesign)
  - eventos/static/eventos/css/eventos.css (modern professional styles)
- Fixed URL routing (eventos/ now properly routes to main page)

### Environment Setup
- Installed Python 3.11 module
- Configured environment variables (SECRET_KEY, FERNET_KEY, DEBUG=True)
- Modified settings.py for Replit compatibility
- Set up in-memory channels layer for WebSockets
- Configured workflow to run on port 5000

### Mobile Responsive Design
- Added comprehensive CSS media queries for mobile devices
- Hid sidebar panels (left and right) on screens < 1024px
- Created professional bottom navigation menu for mobile with 5 items:
  - Feed (Home icon)
  - Perfil (User icon)
  - Gamificação (Badge icon, abbreviated as "Gamif." on mobile)
  - Eventos (Calendar icon)
  - Chat (Message icon)
- Professional SVG icons instead of emojis:
  - Clean, modern outline icons
  - Properly sized at 24x24px
  - Stroke-based with configurable weight
  - Aria-hidden for accessibility (labels on parent elements)
- Advanced navbar styling:
  - Gradient background with backdrop-filter blur effect
  - Active state indicator (blue bar at top of active item)
  - Smooth hover effects with light blue background
  - Cubic-bezier transitions for premium feel
- Overflow prevention:
  - overflow-x: hidden on html, body, and all containers
  - max-width constraints on all responsive elements
  - Flex-wrap on post options to prevent horizontal scroll
- Full ARIA accessibility support for navigation items
- Safe-area padding for notched devices (iOS/Android)
- Responsive breakpoints at 1024px (tablet), 640px (phone), and 380px (small phone)
- All sidebar menu items accessible through bottom navigation on mobile

### Database
- **Current**: PostgreSQL (DATABASE_URL with Replit's built-in database)
- All 58 migrations applied successfully
- Test tenant: "MySphere Corp" (ID: 1)
- Test user: teste@mysphere.com (password: teste123)
- Sample data: 5 eventos created for testing
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
- Database is now PostgreSQL (no need for unset DATABASE_URL)

### Mobile-First Design
- Prioritize mobile experience with clean, minimalist UI
- Hide unnecessary elements on small screens
- Use bottom navigation for easy thumb access on mobile devices

## Running the Application

### Development Server
The Django development server is configured to run on `0.0.0.0:5000` to work with Replit's proxy system.

Workflow command:
```bash
python3.11 manage.py runserver 0.0.0.0:5000
```

### Test Login Credentials
- Email: teste@mysphere.com
- Password: teste123
- Tenant: MySphere Corp

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
- Static files must be collected after CSS/JS changes (run: `python3.11 manage.py collectstatic --noinput`)
- Server must be running to see updates in the web preview
- Mobile view activates at screen width < 1024px
- Eventos page requires login - use test credentials above

## Next Steps
- Consider migrating to PostgreSQL for production
- Add more interactive features to bottom navigation
- Optimize image loading for mobile devices
- Implement progressive web app (PWA) features
