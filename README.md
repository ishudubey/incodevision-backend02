# JWT Authentication Project - Task 02

![Project Logo](link-to-your-logo-or-screenshot)  

## Overview
This project implements **JWT-based authentication** using **Django** and **Django REST Framework**. It allows users to **register, login, refresh tokens, and access protected endpoints** securely. This project was completed as **Task 02** during my internship at **IncodeVision**.

## Features
- User registration and login with email/password.
- Access and refresh tokens for secure authentication.
- Protected API endpoints accessible only with valid JWT.
- Token expiration handling.
- Simple, scalable backend structure using Django and DRF.

## Tech Stack
- Python 3.11+
- Django 5.2
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (for development)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ishudubey/incodevision-backend02.git
cd incodevision-backend02
Create and activate virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Apply migrations

python manage.py makemigrations
python manage.py migrate
Run the development server

python manage.py runserver
Access the APIs

Base URL: http://127.0.0.1:8000/api/

API Endpoints
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/token/	Get access and refresh tokens
POST	/api/token/refresh/	Refresh access token
GET	/api/profile/	Access protected user profile info
Sample JSON Request for Registration

{
  "username": "ishu",
  "email": "ishu@example.com",
  "password": "StrongPassword123"
}
Sample JSON Response for Token

{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
Screenshots
1. Registration API in Postman

2. Login & JWT tokens

3. Protected Profile Endpoint

How to Test
Register a user using /api/register/.

Login using /api/token/ to get access and refresh tokens.

Use the access token in the Authorization header (Bearer <token>) to access /api/profile/.

Refresh access token using /api/token/refresh/ if it expires.

Author
Ishu Dubey – Backend Developer Intern at IncodeVision

GitHub: https://github.com/ishudubey

LinkedIn: https://www.linkedin.com/in/ishu-dubey-59a282383 

