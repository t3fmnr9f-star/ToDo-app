# ToDo App
A simple **API-first** ToDo app built with Django and the Django REST Framework.
Users can create, edit, delete, and search their ToDo items.
All operations are done via the API and **session-based authentication** is used to stay logged in.

#### Technologies
- Python 3.9+
- Django 4+
- Django REST Framework
- Session-based authentication
- Postman (for API testing)

---

## Installation and Setup

1. **Clone the project**

```bash
git clone https://github.com/username/todo-app.git
cd todo-app
```

2. **Create and activate the virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Migrating the database**

```bash
python manage.py migrate
```

5. **Create superuser (optional for admin)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

---
---

## API details
Full details of endpoints and sample request/response are available in the documentation file: [LINK](Docs/API_DOC.md)

### Features:
* Create, view, edit and delete items
* Search on `title` and `content`
* Sort (`updated_at` or `title`)

---

## API testing
You can use Postman Collection to test all endpoints. [LINK](Docs/postman_collection.json)

Postman Collection contains everything:<br>
Signup<br>
Login<br>
Logout<br>
Get Todos: View user's Todos<br>
Create Todo<br>
Update Todo: with PUT or PATCH<br>
Delete Todo<br>
Search Todos: Search by title and content<br>
Sort Todos: Sort by updated_at or title

How to use:<br>
open the Postman → File → Import → Select JSON file<br>
All requests are ready to test

---
I also designed the frontend. You can see it in this repo:
LINK

And I also deployed the site. You can test it in this link:
LINK

