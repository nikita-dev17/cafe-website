# Cafe Website

A simple coffee shop website built with **Flask**.  
Includes a public website and an admin panel for managing menu items.


## Screenshots

### Public pages

#### Home
![Home](screenshots/home.png)

#### About us
![About](screenshots/about_us.png)

#### Menu
![Menu](screenshots/menu.png)

---

### Admin panel

#### Login
![Admin login](screenshots/admin_login.png)

#### Dashboard
![Admin dashboard](screenshots/admin_dashboard.png)

#### Add / Edit meal
![Add meal](screenshots/add_meal.png)
![Edit meal](screenshots/edit_meal.png)



## Features

- Public pages (home, menu, about)
- UI built with Bootstrap
- Admin panel
- CRUD operations for menu items
- Password hashing with Flask-Bcrypt
- Database with Flask-SQLAlchemy
- Environment variables support with python-dotenv
- Modular structure using Blueprints

## Tech Stack
- Python
- Flask (Blueprints)
- Flask-SQLAlchemy
- Flask-Bcrypt
- Jinja2
- Bootstrap 5
- SQLite

## Installation & Run

```bash
# Clone the repository
git clone https://github.com/nikita-dev17/cafe-website.git
cd cafe-website

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Environment variables
cp .env.example .env
# Edit .env if needed

# Run the application
python -m cafe_website.app

