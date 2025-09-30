# API_DOC.md

````markdown
# ToDo API Documentation

این مستندات شامل همه endpointهای پروژه ToDo است.

---

## 🔑 احراز هویت

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

* **Response:** کوکی session ست می‌شود

---

### Logout

* **URL:** `/api-auth/logout/`
* **Method:** POST
* **Response:** کوکی session پاک می‌شود

---

## 🗂️ Todo Endpoints

> **توجه:** فقط آیتم‌های کاربر لاگین‌شده قابل مشاهده هستند.

### Get Todos

* **URL:** `/api/todos/`
* **Method:** GET
* **Query Params:**

  * `search` (اختیاری): جستجو در title و content
  * `ordering` (اختیاری): مرتب‌سازی بر اساس `updated_at` یا `title`
* **Response (200):**

```json
[
  {
    "id": 1,
    "title": "خرید میوه",
    "content": "سیب و پرتقال",
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
  "title": "مثال",
  "content": "توضیح"
}
```

* **Response (201):**

```json
{
  "id": 2,
  "title": "مثال",
  "content": "توضیح",
  "completed": false,
  "updated_at": "2025-09-30T12:40:00Z"
}
```

### Update Todo

* **URL:** `/api/todos/{id}/`
* **Method:** PATCH
* **Body (نمونه تغییر وضعیت):**

```json
{
  "completed": true
}
```

* **Response (200):**

```json
{
  "id": 2,
  "title": "مثال",
  "content": "توضیح",
  "completed": true,
  "updated_at": "2025-09-30T12:45:00Z"
}
```

### Delete Todo

* **URL:** `/api/todos/{id}/`
* **Method:** DELETE
* **Response (204):** بدون محتوا

---

## 🔍 جستجو و مرتب‌سازی

* **جستجو:** `GET /api/todos/?search=کلیدواژه`
* **مرتب‌سازی:** `GET /api/todos/?ordering=-updated_at` یا `?ordering=title`

---

**توجه:** تمام درخواست‌ها بعد از لاگین با session معتبر انجام می‌شوند.

```
