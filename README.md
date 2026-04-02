# Cinema Management System

A comprehensive Django-based cinema management system for handling rooms, films, projections, and ticket sales with an interactive seat selection interface.

## Features

### Core Functionality

- **Room Management (Sale)**: Create, read, update, and delete cinema rooms with configurable seat layouts
- **Film Catalog**: Manage a comprehensive film database with filtering by genre and year
- **Projection Scheduling**: Schedule film projections in specific rooms with pricing
- **Ticket Management**: Track ticket availability, sales, and reservations with interactive seat grid visualization
- **Interactive Seat Grid**: Visual representation of theater seats with status indicators (available, reserved, sold)

### Technical Features

- Professional white-themed Bootstrap 5 interface
- Responsive design for desktop and mobile devices
- Database-driven with SQLite
- Django ORM for data management
- URL routing for clean, RESTful-style URLs
- Template inheritance for consistent UI
- Form-based CRUD operations
- Filtering and search capabilities

## Project Structure

```
cinema_project/
├── cinema_project/          # Main project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── templates/              # Global templates
│   └── base.html          # Base template with Bootstrap 5
├── static/                # Static files (CSS, JS, images)
├── homepage/              # Homepage app
│   ├── views.py          # Dashboard view
│   ├── urls.py           # Homepage URLs
│   └── templates/
│       └── homepage/index.html
├── sale/                  # Room management app
│   ├── models.py         # Sala (Room) model
│   ├── views.py          # CRUD operations
│   ├── urls.py           # Room URLs
│   └── templates/sale/
│       ├── lista.html    # Room listing
│       ├── form.html     # Create/Edit form
│       └── dettaglio.html # Room details
├── film/                  # Film catalog app
│   ├── models.py         # Film model
│   ├── views.py          # CRUD with filtering
│   ├── urls.py           # Film URLs
│   └── templates/film/
│       ├── lista.html    # Film listing with filters
│       ├── form.html     # Create/Edit form
│       └── dettaglio.html # Film details
├── proiezioni/           # Projection scheduling app
│   ├── models.py         # Proiezione (Projection) model
│   ├── views.py          # CRUD operations
│   ├── urls.py           # Projection URLs
│   └── templates/proiezioni/
│       ├── lista.html    # Projection listing
│       ├── form.html     # Create/Edit form
│       └── dettaglio.html # Projection details with seat grid
├── biglietti/            # Ticket management app
│   ├── models.py         # Biglietto (Ticket) model
│   ├── views.py          # Ticket operations
│   ├── urls.py           # Ticket URLs
│   └── templates/biglietti/
│       ├── lista.html    # Ticket listing with filters
│       └── dettaglio.html # Ticket details
├── manage.py             # Django management script
└── populate_data.py      # Data population script
```

## Database Models

### Sala (Room)
- `nome`: Room name
- `numero_posti`: Total number of seats
- `numero_file`: Number of rows
- `posti_per_fila`: Seats per row
- `created_at`, `updated_at`: Timestamps

### Film
- `titolo`: Film title
- `descrizione`: Film description
- `regista`: Director name
- `genere`: Genre
- `durata_minuti`: Duration in minutes
- `anno_uscita`: Release year
- `rating`: Rating (0-10)
- `created_at`, `updated_at`: Timestamps

### Proiezione (Projection)
- `sala`: Foreign key to Sala
- `film`: Foreign key to Film
- `data_ora`: Projection date and time
- `prezzo_biglietto`: Ticket price
- `posti_disponibili`: Available seats count
- `created_at`, `updated_at`: Timestamps

### Biglietto (Ticket)
- `proiezione`: Foreign key to Proiezione
- `numero_fila`: Row letter (A, B, C, etc.)
- `numero_posto`: Seat number
- `stato`: Ticket status (available, reserved, sold)
- `prezzo`: Ticket price
- `data_vendita`: Sale date/time
- `created_at`, `updated_at`: Timestamps

## Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation Steps

1. **Create and activate virtual environment**:
   ```bash
   python3.11 -m venv cinema_venv
   source cinema_venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install django==5.2.7 django-filter
   ```

3. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Populate sample data** (optional):
   ```bash
   python manage.py shell < populate_data.py
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

6. **Access the application**:
   - Open browser and navigate to `http://localhost:8000/`

## Usage Guide

### Homepage
- Dashboard showing statistics: number of rooms, films, projections, and tickets
- Quick navigation to all management sections

### Room Management (Sale)
- **View Rooms**: List all cinema rooms with seat counts
- **Create Room**: Add new room with custom layout
- **Edit Room**: Modify room details
- **Delete Room**: Remove rooms (with confirmation)
- **View Details**: See room information and associated projections

### Film Catalog
- **Browse Films**: View all films with details (director, genre, duration, rating)
- **Filter Films**: Filter by genre and release year
- **Create Film**: Add new films to catalog
- **Edit Film**: Update film information
- **Delete Film**: Remove films from catalog
- **View Details**: See full film information and associated projections

### Projection Scheduling
- **Schedule Projection**: Create new projection linking room, film, date/time, and price
- **Automatic Ticket Generation**: Tickets are automatically created for all seats when projection is created
- **View Projections**: List all scheduled projections with availability status
- **Interactive Seat Grid**: Visual representation of theater layout with seat status
- **Modify Projection**: Update projection details (date, time, price)
- **Cancel Projection**: Remove scheduled projections

### Ticket Management
- **Browse Tickets**: View all tickets across all projections
- **Filter Tickets**: Filter by projection and ticket status
- **Ticket Details**: View individual ticket information
- **Sell Ticket**: Mark ticket as sold and record sale date
- **Release Ticket**: Return sold/reserved tickets to available status
- **Status Indicators**: 
  - Green: Available for purchase
  - Orange: Reserved
  - Gray: Sold

## UI Design

### Color Scheme
- **Primary**: #2c3e50 (Dark Blue-Gray) - Headers and text
- **Secondary**: #3498db (Light Blue) - Buttons and accents
- **Accent**: #e74c3c (Red) - Delete actions
- **Background**: #ffffff (White) - Clean, professional look
- **Light Background**: #f8f9fa (Light Gray) - Sections and filters

### Typography
- **Font Family**: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- **Professional appearance** with proper spacing and hierarchy

### Components
- **Navbar**: Sticky navigation with links to all sections
- **Cards**: Organized information display with hover effects
- **Tables**: Responsive tables for data listing
- **Forms**: Clean, accessible form inputs
- **Badges**: Status indicators for different states
- **Seat Grid**: Interactive grid layout for theater visualization

## API Routes

### Homepage
- `GET /` - Dashboard

### Rooms (Sale)
- `GET /sale/` - List rooms
- `GET /sale/crea/` - Create room form
- `POST /sale/crea/` - Submit new room
- `GET /sale/<id>/` - View room details
- `GET /sale/<id>/modifica/` - Edit room form
- `POST /sale/<id>/modifica/` - Submit room update
- `GET /sale/<id>/elimina/` - Delete room

### Films
- `GET /film/` - List films (with filters)
- `GET /film/crea/` - Create film form
- `POST /film/crea/` - Submit new film
- `GET /film/<id>/` - View film details
- `GET /film/<id>/modifica/` - Edit film form
- `POST /film/<id>/modifica/` - Submit film update
- `GET /film/<id>/elimina/` - Delete film

### Projections
- `GET /proiezioni/` - List projections
- `GET /proiezioni/crea/` - Create projection form
- `POST /proiezioni/crea/` - Submit new projection
- `GET /proiezioni/<id>/` - View projection with seat grid
- `GET /proiezioni/<id>/modifica/` - Edit projection form
- `POST /proiezioni/<id>/modifica/` - Submit projection update
- `GET /proiezioni/<id>/elimina/` - Delete projection

### Tickets
- `GET /biglietti/` - List tickets (with filters)
- `GET /biglietti/<id>/` - View ticket details
- `GET /biglietti/<id>/vendi/` - Sell ticket
- `GET /biglietti/<id>/libera/` - Release ticket

## Sample Data

The `populate_data.py` script creates:
- **3 Rooms**: Premium (100 seats), Standard (80 seats), Small (50 seats)
- **5 Films**: Dune: Part Two, Oppenheimer, Barbie, Killers of the Flower Moon, The Brutalist
- **6 Projections**: Various combinations of films and rooms
- **460 Tickets**: Automatically generated for all seats

## Customization

### Adding Custom Styling
- Edit `/home/ubuntu/templates/base.html` to modify CSS variables
- Add custom CSS in the `<style>` section

### Modifying Seat Layout
- Update `numero_file` and `posti_per_fila` in room creation
- Seat labels are automatically generated (A1, A2, B1, etc.)

### Extending Functionality
- Add new models to individual app `models.py`
- Create views in app `views.py`
- Add URL patterns in app `urls.py`
- Create templates in app `templates/` directory

## Troubleshooting

### Template Not Found
- Ensure `TEMPLATES['DIRS']` includes `BASE_DIR / 'templates'` in settings.py
- Check that template files exist in correct directories

### Static Files Not Loading
- Run `python manage.py collectstatic` if needed
- Ensure `STATIC_URL` and `STATICFILES_DIRS` are configured

### Database Errors
- Run migrations: `python manage.py migrate`
- Check database file exists: `db.sqlite3`

## Performance Considerations

- Database is optimized with proper indexing through Django ORM
- Seat grid uses CSS Grid for efficient rendering
- Filtering uses Django QuerySet filtering for database-level optimization
- Template inheritance reduces code duplication

## Security Notes

- DEBUG = True in development (should be False in production)
- ALLOWED_HOSTS = ['*'] in development (should be restricted in production)
- CSRF protection enabled on all forms
- SQL injection protected through Django ORM

## Future Enhancements

- User authentication and authorization
- Admin panel for staff management
- Payment integration for online ticket sales
- Email notifications for bookings
- Advanced analytics and reporting
- Mobile app version
- Real-time seat availability updates
- Customer account management
- Booking history and receipts

## License

This project is provided as-is for educational and commercial use.

## Support

For issues or questions, refer to Django documentation:
- Django Official: https://www.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/5.2/topics/db/models/
- Django Views: https://docs.djangoproject.com/en/5.2/topics/http/views/
- Bootstrap 5: https://getbootstrap.com/docs/5.3/

---

**Created**: April 2, 2026  
**Version**: 1.0.0  
**Framework**: Django 5.2.7  
**Database**: SQLite3
