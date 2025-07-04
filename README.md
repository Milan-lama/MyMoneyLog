# MyMoneyLog

**MyMoneyLog** is a personal expense tracking web application built with Django and Django REST Framework. It allows users to log, manage, and monitor their daily expenses efficiently with user authentication and API endpoints.

---

## 🔍 Overview

The goal of this project is to provide users with a simple platform to:

- Register and authenticate
- Record their expenses
- Categorize and view their spending
- Interact with RESTful APIs

---

## 🚀 Features

- User Registration and Login
- JWT-based Authentication
- Add, Edit, and Delete Expense Entries
- API endpoints for integration with frontend/mobile
- Modular Django app structure (`users`, `expenses`)

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (for development)
- **Auth**: JWT Authentication (via DRF)

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd MyMoneyLog
```

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```
### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```
### 6. Run Development Server

```bash
python manage.py runserver
```

## 🧪 Usage

- Visit `http://127.0.0.1:8000/` to access the project.
- Use tools like **Postman** to interact with the API endpoints.
- Register/login to access user-specific expense logs.

---

## 📡 API Endpoints 

| Endpoint             | Method | Description            |
|----------------------|--------|------------------------|
| `/api/auth/register/`   | POST   | Register new users     |
| `/api/auth/login/`      | POST   | Authenticate users     |
| `/api/auth/refresh/`      | POST   | Refresh and obtain a new access token  |
| `/api/expenses/`         | GET    | List all expenses      |
| `/api/expenses/<id>/`         | GET    | Get specific expense      |
| `/api/expenses/<id>/`    | PUT    | Update an expense      |
| `/api/expenses/<id>/`    | DELETE | Delete an expense      |

> **Note:** For authentication, include your token in the headers:  
> `Authorization: Token <your-token>`


## 📬 API Testing with Postman

### 🔐 User Registration (`/api/auth/register/`)

![Register API](postman_images/register.png)

---

### 🔑 User Login (`/api/auth/login/`)

![Login API](postman_images/login.png)

---

### 🔄 Refresh Token (`/api/auth/refresh/`)

![Refresh Token API](postman_images/refresh_token.png)


---

### ➕ Add New Expense (`/api/expenses/` – POST)

![Add Expense API](postman_images/add_expense.png)


---

### 📥 Get All Expenses (`/api/expenses/` – GET)

![Get Expenses API](postman_images/get_expenses.png)

---

### 📄 Get Single Expense (`/api/expenses/<id>/` – GET)

![Get Single Expense API](postman_images/get_single_expense.png)

> 📌 Example: `GET /expenses/3/` to retrieve the expense with ID 3.

---

### ✏️ Update Expense (`/api/expenses/<id>/` – PUT)

![Update Expense API](postman_images/update_expense.png)


---

### ❌ Delete Expense (`/api/expenses/<id>/` – DELETE)

![Delete Expense API](postman_images/delete_expense.png)

> 📌 Example: `DELETE /expenses/3/` to delete the expense with ID 3.


---

## 📁 Project Structure

```bash
MyMoneyLog/
│
├── expenses/           # Expense tracking app
├── users/              # User authentication app
├── MyMoneyLog/         # Main Django project config
├── postman_images/     # Api testing images
├── requirements.txt    # Python dependencies
├── manage.py           # Django management script


## 🌟 Future Improvements

- Add expense categories and tags  
- Generate expense reports and charts  
- Search and filter expenses  
- Export expenses as PDF/CSV  
- Mobile-friendly frontend with React or Flutter  
- Dark mode support  

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve **MyMoneyLog**, feel free to:

1. Fork the repository  
2. Create a new feature branch  
3. Submit a pull request  

Please ensure your code follows project conventions and is properly tested.

---

## 📝 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

