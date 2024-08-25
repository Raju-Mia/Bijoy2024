# Django API Project -Bijoy2024

This project provides an API for user management using Django and Django REST Framework (DRF). It includes endpoints for user registration, login, listing users, and managing individual user details.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Raju-Mia/Bijoy2024.git
    ```

2. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### **1. Sign-Up**

- **URL:** `/signup/`
- **Method:** `POST`
- **Description:** Registers a new user and returns JWT tokens.
- **Request JSON:**
    ```json
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword"
    }
    ```
- **Response JSON (Success):**
    ```json
    {
        "refresh": "your-refresh-token",
        "access": "your-access-token",
        "user_id": 1,
        "email": "newuser@example.com"
    }
    ```
- **Response JSON (Error):**
    ```json
    {
        "username": [
            "This field is required."
        ],
        "email": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }
    ```

### **2. Login**

- **URL:** `/login/`
- **Method:** `POST`
- **Description:** Authenticates a user and returns JWT tokens.
- **Request JSON:**
    ```json
    {
        "email": "existinguser@example.com",
        "password": "securepassword"
    }
    ```
- **Response JSON (Success):**
    ```json
    {
        "message": "Login successful",
        "refresh": "your-refresh-token",
        "access": "your-access-token"
    }
    ```
- **Response JSON (Error - Invalid Credentials):**
    ```json
    {
        "error": "Invalid credentials"
    }
    ```
- **Response JSON (Error - Validation Errors):**
    ```json
    {
        "email": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }
    ```

### **3. List Users**

- **URL:** `/users/`
- **Method:** `GET`
- **Description:** Retrieves a list of all users. Requires authentication.
- **Response JSON:**
    ```json
    [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com"
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com"
        }
    ]
    ```

### **4. Create User**

- **URL:** `/users/`
- **Method:** `POST`
- **Description:** Creates a new user. Requires authentication.
- **Request JSON:**
    ```json
    {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword"
    }
    ```
- **Response JSON (Success):**
    ```json
    {
        "id": 3,
        "username": "newuser",
        "email": "newuser@example.com"
    }
    ```
- **Response JSON (Error):**
    ```json
    {
        "username": [
            "This field is required."
        ],
        "email": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }
    ```

### **5. Retrieve User Details**

- **URL:** `/users/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieves a user by ID. Requires authentication and proper permissions.
- **Response JSON:**
    ```json
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com"
    }
    ```

### **6. Update User Details**

- **URL:** `/users/<int:pk>/`
- **Method:** `PUT`
- **Description:** Updates a user by ID. Requires authentication and proper permissions.
- **Request JSON:**
    ```json
    {
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    ```
- **Response JSON (Success):**
    ```json
    {
        "id": 1,
        "username": "updateduser",
        "email": "updateduser@example.com"
    }
    ```
- **Response JSON (Error):**
    ```json
    {
        "username": [
            "This field is required."
        ],
        "email": [
            "This field is required."
        ]
    }
    ```

### **7. Delete User**

- **URL:** `/users/<int:pk>/`
- **Method:** `DELETE`
- **Description:** Deletes a user by ID. Requires authentication and proper permissions.
- **Response JSON (Success):**
    ```json
    {
        "message": "User Delete Successfully"
    }
    ```

## Custom Permissions

- **`IsOwnerOrReadOnly`**: Custom permission that ensures only the owner or admin can update or delete a user.

## Dependencies

- Django
- Django REST Framework
- djangorestframework-simplejwt

Ensure all dependencies are listed in `requirements.txt`.

## Author

- **Author:** Raju-Mia
- **Website:** [www.rajumia.com](https://www.rajumia.com)
