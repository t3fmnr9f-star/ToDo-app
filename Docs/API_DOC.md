# API_DOC.md

````markdown
# ToDo API Documentation

This documentation includes all the endpoints of the ToDo project.

---

## 🔑 Authentication

### Signup
- **URL:** `/api/signup/`
- **Method:** POST
- **Body:**
```json
{
"username": "newuser",
"password": "newpassword"
}
````

* **Response (201):**

```json
{
"message": "User created successfully"
}
```

---

### Login

* **URL:** `/api-auth/login/`
* **Method:** POST
* **Body (x-www-form-urlencoded):**

```
username=newuser
password=newpassword
```

* **Response:** Session cookie set

---

### Logout

* **URL:** `/api-auth/logout/`
* **Method:** POST
* **Response:** Session cookie cleared

---

## 🗂️ Todo Endpoints

> **Note:** Only logged-in user items are visible.

### Get Todos

* **URL:** `/api/todos/`
* **Method:** GET
* **Query Params:**

* `search` (optional): Search in title and content
* `ordering` (optional): Sort by `updated_at` or `title`
* **Response (200):**

```json
[
{
"id": 1,
"title": "Buy Fruit",
"content": "Apple and Orange",
"completed": false,
"updated_at": "2025-09-30T12:34:56Z"
}
]
```

### Create Todo

* **URL:** `/api/todos/`
* **Method:** POST
* **Body:**

```json
{
"title": "Example",
"content": "Explanation"
}
```

* **Response (201):**

```json
{
"id": 2,
"title": "Example",
"content": "Explanation",
"completed": false,
"updated_at": "2025-09-30T12:40:00Z"
}
```

### Update Todo

* **URL:** `/api/todos/{id}/`
* **Method:** PATCH
* **Body (Example of the status change):**

```json
{
"completed": true
}
```

* **Response (200):**

```json
{
"id": 2,
"title": "Example",
"content": "Explanation",
"completed": true,
"updated_at": "2025-09-30T12:45:00Z"
}
```

### Delete Todo

* **URL:** `/api/todos/{id}/`
* **Method:** DELETE
* **Response (204):** No content

---

## 🔍 Search and Sort

* **Search:** `GET /api/todos/?search=keyword`
* **Sort:** `GET /api/todos/?ordering=-updated_at` or `?ordering=title`


**Note:** All requests are made after login with a valid session.


