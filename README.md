# Cafe Website

A simple coffee shop website built with **Flask**.  
Includes a public website and an admin panel for managing menu items.

## Features

- Public pages (home, menu, about)
- Admin panel
- CRUD operations for menu items
- Password hashing with Flask-Bcrypt
- Database with Flask-SQLAlchemy
- Environment variables support with python-dotenv
- Modular structure using Blueprints

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Jinja2
- SQLite

## Installation & Run


### Clone the repository
git clone https://github.com/nikita-dev17/cafe-website.git
cd cafe-website

### Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Environment variables
Create a .env file in the project root based on .env.example
and set the required variables.

### Run the application
python -m cafe_website.app
