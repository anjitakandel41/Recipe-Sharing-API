# 🍽️ Recipe Sharing API

A backend REST API built with **Django** and **Django REST Framework** that allows users to create, browse, update, and delete recipes with image uploads. The project also includes JWT authentication, email notifications, Swagger documentation, and a customized Jazzmin admin panel.

## 🚀 Features

* User authentication using JWT
* Create, read, update, and delete recipes
* Upload recipe photos
* Browse recipes by category
* Search recipes by title
* Email confirmation when a recipe is published
* Swagger and ReDoc interactive API documentation
* Jazzmin-themed Django Admin
* Owner-only update and delete permissions
* Environment variable configuration using `.env`

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* drf-yasg (Swagger/ReDoc)
* Jazzmin
* Pillow
* django-filter
* django-environ
* SQLite

---

## 📁 Project Structure

```text
Recipe-sharing-api/
├── config/
├── recipes/
├── media/
├── staticfiles/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <your-private-repository-url>
cd Recipe-sharing-api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

---

# 🔑 Authentication

This project uses JWT Authentication.

## Obtain Token

```http
POST /api/token/
```

Request:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Response:

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

---

## Refresh Token

```http
POST /api/token/refresh/
```

Request:

```json
{
    "refresh": "your_refresh_token"
}
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/swagger/
```

ReDoc:

```text
http://127.0.0.1:8000/redoc/
```

---

# 📌 API Endpoints

## Recipes

| Method | Endpoint             | Description     |
| ------ | -------------------- | --------------- |
| GET    | `/api/recipes/`      | List recipes    |
| POST   | `/api/recipes/`      | Create recipe   |
| GET    | `/api/recipes/{id}/` | Retrieve recipe |
| PUT    | `/api/recipes/{id}/` | Update recipe   |
| PATCH  | `/api/recipes/{id}/` | Partial update  |
| DELETE | `/api/recipes/{id}/` | Delete recipe   |

---

## Categories

| Method | Endpoint                | Description       |
| ------ | ----------------------- | ----------------- |
| GET    | `/api/categories/`      | List categories   |
| POST   | `/api/categories/`      | Create category   |
| GET    | `/api/categories/{id}/` | Retrieve category |
| PUT    | `/api/categories/{id}/` | Update category   |
| DELETE | `/api/categories/{id}/` | Delete category   |

---

# 🔍 Search and Filtering

Search recipes by title:

```http
GET /api/recipes/?search=cake
```

Filter by category:

```http
GET /api/recipes/?category=1
```

---

# 📤 File Upload Example

Create Recipe:

```http
POST /api/recipes/
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

Fields:

```text
title=Chicken Momo
description=Traditional Nepali dumplings
ingredients=Flour, Chicken, Onion
steps=Prepare filling and steam
cooking_time=30
category=1
photo=<image_file>
```

---

# 📧 Email Notification

When a recipe is successfully published, the author receives a confirmation email.

Example:

Subject:

```text
Recipe Published Successfully
```

Body:

```text
Your recipe has been published successfully.
```

---

# 🔒 Permissions

* Anyone can view recipes and categories.
* Authenticated users can create recipes.
* Only the recipe owner can update or delete their own recipes.
* Unauthorized requests return `401 Unauthorized`.
* Forbidden actions return `403 Forbidden`.

---

# 👨‍💼 Admin Panel

Admin URL:

```text
http://127.0.0.1:8000/admin/
```

Features:

* Jazzmin-themed admin interface
* list_display
* search_fields
* list_filter
* readonly_fields
* Inline editing using TabularInline

---

## Jazzmin Admin Panel

```markdown

<img width="1887" height="968" alt="image" src="https://github.com/user-attachments/assets/df87220c-edf5-4981-a7e6-d19fec0aa4e7" />
<img width="1918" height="902" alt="image" src="https://github.com/user-attachments/assets/0750f3fc-0399-46e0-8fb1-799121814ab1" />
<img width="1916" height="915" alt="image" src="https://github.com/user-attachments/assets/1f081d5c-e213-4fe2-95e4-fed7a65ad3a0" />

)
```


## Swagger Documentation

```markdown
![Swagger UI](<img width="1802" height="851" alt="image" src="https://github.com/user-attachments/assets/747bfcf4-cc72-47ab-900f-8fc63842e5d3" />
<img width="1746" height="821" alt="image" src="https://github.com/user-attachments/assets/00153610-6d6b-418a-9ded-8da24d8a5ef6" />
<img width="1832" height="888" alt="image" src="https://github.com/user-attachments/assets/212b9c14-f0f3-4178-918b-b796d4309096" />
<img width="1786" height="886" alt="image" src="https://github.com/user-attachments/assets/47020c2d-e28e-4431-8bbf-b630945161a8" />



)
```

## JWT Token Generation

```markdown
![JWT Authentication](<img width="827" height="473" alt="image" src="https://github.com/user-attachments/assets/8fc8652f-7b65-40d4-a270-62c96028e5e9" />
<img width="845" height="478" alt="image" src="https://github.com/user-attachments/assets/20744385-37e9-4171-ba4a-5f9c9f3d636c" />

)
```


## Email Sent Successfully

```markdown
![Email Confirmation](<img width="1856" height="672" alt="image" src="https://github.com/user-attachments/assets/3bad838b-97d3-43a9-8321-865ec9b2d0ce" />
)
```



