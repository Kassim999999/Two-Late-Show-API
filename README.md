# Two Late Show API 

A RESTful Flask API for managing a fictional late-night talk show. It supports user registration and login (JWT-based), and CRUD operations for episodes, guests, and their appearances.

---

## Tech Stack

- **Backend**: Python, Flask
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Authentication**: JWT (Flask-JWT-Extended)
- **Migrations**: Flask-Migrate

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Kassim999999/Two-Late-Show-API
cd Two-late-show-API
```

### 2. Create and activate virtual environment (using pipenv or venv)

```bash
pipenv shell
# OR
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. PostgreSQL setup

Ensure PostgreSQL is running.

Create the database:

```bash
createdb late_show_db
```

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://your_user:your_password@localhost/late_show_db
JWT_SECRET_KEY=your_super_secret_key
```

Update `config.py` to use these env vars.

---

## Running the App

### 1. Migrate the database

```bash
flask db init    
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the database

```bash
python server/seed.py
```

### 3. Run the server

```bash
flask run
```

Server will be available at `http://127.0.0.1:5000`

---

## Auth Flow

### 🔸 Register

**POST** `/register`

```json
{
  "username": "host123",
  "email": "host@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "User registered successfully"
}
```

---

### 🔸 Login

**POST** `/login`

```json
{
  "username": "host123",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "JWT_TOKEN",
  "user_id": 1
}
```

Use the token in `Authorization` header for protected routes:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## API Endpoints

### Guests

| Method | Endpoint       | Description            |
|--------|----------------|------------------------|
| GET    | /guests        | Get all guests         |
| POST   | /guests        | Create a guest         |
| GET    | /guests/<id>   | Get guest by ID        |
| PATCH  | /guests/<id>   | Update a guest         |
| DELETE | /guests/<id>   | Delete a guest         |

---

### Episodes

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | /episodes        | Get all episodes         |
| POST   | /episodes        | Create an episode        |
| GET    | /episodes/<id>   | Get episode by ID        |
| PATCH  | /episodes/<id>   | Update an episode        |
| DELETE | /episodes/<id>   | Delete an episode        |

---

### Appearances

| Method | Endpoint            | Description                    |
|--------|---------------------|--------------------------------|
| GET    | /appearances        | List all appearances           |
| POST   | /appearances        | Create a new appearance        |
| GET    | /appearances/<id>   | Get appearance details         |
| PATCH  | /appearances/<id>   | Update an appearance           |
| DELETE | /appearances/<id>   | Delete an appearance           |

---

## Postman Usage Guide

1. Import your API collection in Postman.
2. Create a request to `/register` to sign up.
3. Then use `/login` to retrieve a JWT.
4. Set an environment variable in Postman for `JWT_TOKEN` or add this header to each request:
```
Authorization: Bearer YOUR_TOKEN_HERE
```
5. Now you can access protected routes (like creating guests, episodes, etc.).

**Tip**: Save your token in Postman's environment and use `{{JWT_TOKEN}}` in the header.

---

## GitHub Repo

[🔗 GitHub Repository](https://github.com/Kassim999999/Two-Late-Show-API)

> Replace `YOUR-USERNAME` with your actual GitHub username.

---

## Future Features

- User roles (admin/host)
- Image upload for guests
- Pagination & filtering
- Frontend integration

---

## Contact

Built by Rooney Kassim
