# Booking System Web App

A web-based booking and appointment management system built with Django and PostgreSQL.

## Tech Stack

- Python
- Django
- PostgreSQL
- HTML/CSS
- Bootstrap5

---

## Features

### Core Features

- User booking system
- Admin dashboard
- Email confirmation system
- Store and manage appointments



## Installation

### 1. Clone the repository

```bash
git clone https://github.com/zen085/booking-system.git
cd booking-system
```

---

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_django_secret_key

DB_NAME=booking_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 3. Install Dependencies

Install all required project packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6. Start the Development Server

```bash
python manage.py runserver
```

The app will run locally at:

```bash
http://127.0.0.1:8000/
```

---


```

---

## License

This project is licensed under the MIT License.