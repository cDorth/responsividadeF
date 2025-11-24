# MySphere - Replit Setup

## Project Overview
MySphere is a multi-tenant professional social network platform built with Django. It features real-time chat, gamification, events, and a comprehensive feed system for enterprise communication and collaboration.

## Technology Stack
- **Backend Framework**: Django 5.2.6 with Django Channels for WebSocket support
- **ASGI Server**: Daphne 4.1.2
- **Database**: PostgreSQL (with SQLite fallback for development)
- **Real-time Communication**: Redis + Django Channels
- **Authentication**: Django Allauth with social auth support (Google)
- **Python Version**: 3.11

## Key Features
1. **Multi-tenant Architecture**: Each company has isolated data and customization
2. **Real-time Chat**: WebSocket-based chat with file sharing support
3. **Gamification**: Points, achievements, tasks, and leaderboards
4. **Feed System**: Posts, comments, hashtags, mentions, and file attachments
5. **Events Management**: Create and manage company events
6. **Staff Portal**: Administrative dashboard for managing tenants and users

## Environment Variables
The following environment variables are configured:
- `SECRET_KEY`: Django secret key (auto-generated)
- `FERNET_KEY`: Encryption key for sensitive fields (auto-generated)
- `DEBUG`: Set to True for development
- `DATABASE_URL`: (Optional) PostgreSQL connection URL - create via Replit Database tool

## Database Setup
The project is currently using SQLite for development. To use PostgreSQL:
1. Open the Replit Database tool from the left sidebar
2. Create a PostgreSQL database
3. The DATABASE_URL will be automatically set
4. Restart the server workflow

## Running the Project
The server runs automatically via the "Start Server" workflow which:
1. Starts Redis server for Django Channels
2. Runs Django with Daphne ASGI server on port 5000
3. Serves both HTTP and WebSocket connections

## Project Structure
- `accounts/`: User management and authentication
- `chat/`: Real-time messaging system
- `tenants/`: Multi-tenant functionality
- `feed/`: Social feed with posts and interactions
- `gamification/`: Points, tasks, and achievements
- `staff/`: Administrative interface
- `eventos/`: Event management
- `MySphere/`: Main Django configuration

## Development Notes
- Static files are collected automatically in production
- The project uses Django Channels for WebSocket support
- Redis is required for the chat functionality
- Each tenant has customizable branding (logo, color palette)

## Recent Setup Changes (Nov 24, 2025)
1. Added missing Django Channels dependencies (channels, channels-redis, daphne, redis)
2. Fixed ASGI application to properly initialize Django before importing models
3. Fixed async/sync database operations in chat consumers
4. Added SQLite fallback for development when PostgreSQL is not configured
5. Created static directory structure
6. Configured deployment for Replit's autoscale platform
7. Set up environment variables for production-ready operation

## User Preferences
- None recorded yet

## Next Steps for Users
1. (Optional) Create PostgreSQL database via Replit Database tool for production use
2. (Optional) Configure email settings for password reset functionality
3. Create a superuser account: `python3.11 manage.py createsuperuser`
4. Access the admin panel at `/admin/` to set up tenants and initial data
