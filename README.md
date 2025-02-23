# E-Commerce API

This is a REST API for an e-commerce application built using Django and Django REST Framework.

## Admin Pannel Link: https://e-commerce-project-green-ten.vercel.app/admin/

## Example API URL: https://e-commerce-project-green-ten.vercel.app/api/products/


## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```sh
   python manage.py migrate
   ```

4. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Authentication

The API uses JWT authentication. To get a token:

- **Obtain Token:**
  ```http
  POST /api/token/
  ```
  Request Body:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
  Response:
  ```json
  {
    "access": "your_access_token",
    "refresh": "your_refresh_token"
  }
  ```

- **Refresh Token:**
  ```http
  POST /api/token/refresh/
  ```
  Request Body:
  ```json
  {
    "refresh": "your_refresh_token"
  }
  ```

## API Endpoints

### User Registration
- **Register a new user:**
  ```http
  POST /api/register/
  ```

### Categories
- **List all categories:**
  ```http
  GET /api/categories/
  ```
- **Create a new category (Requires authentication):**
  ```http
  POST /api/categories/create/
  ```
- **Retrieve, update, or delete a category by ID (Requires authentication):**
  ```http
  GET /api/categories/{id}/
  PATCH /api/categories/{id}/
  DELETE /api/categories/{id}/
  ```

### Products
- **List all products:**
  ```http
  GET /api/products/
  ```
- **Create a new product (Requires authentication):**
  ```http
  POST /api/products/create/
  ```
- **Retrieve, update, or delete a product by ID (Requires authentication):**
  ```http
  GET /api/products/{id}/
  PATCH /api/products/{id}/
  DELETE /api/products/{id}/
  ```

### Stock
- **List all stock items:**
  ```http
  GET /api/stocks/
  ```
- **Create a new stock record (Requires authentication):**
  ```http
  POST /api/stocks/create/
  ```
- **Retrieve, update, or delete a stock record by ID (Requires authentication):**
  ```http
  GET /api/stocks/{id}/
  PATCH /api/stocks/{id}/
  DELETE /api/stocks/{id}/
  ```


## Environment Variables
Set up the following environment variables in your `.env` file:
```
# Database Settings
DB_NAME=your_db_name
DB_USER=your_user_name
DB_PASSWORD=your_password
DB_HOST=your_db_host
DB_PORT=5432

# Cloudinary
CLOUD_NAME=your_cloud_name
API_KEY=your_api_key
API_SECRET=your_api_secret

# AWS RDS For Database 
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

