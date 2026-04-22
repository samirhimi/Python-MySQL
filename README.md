# Python Flask MySQL CRUD Application

A simple Flask web application that performs CRUD (Create, Read, Update, Delete) operations on a MySQL database.

## Features

- **Create**: Add new users to the database
- **Read**: Retrieve all users or a specific user by ID
- **Update**: Modify user information
- **Delete**: Remove users from the database
- **Validation**: Email uniqueness and required field validation
- **Error Handling**: Comprehensive error handling and responses

## Prerequisites

- Python 3.7+
- MySQL Server running
- pip (Python package manager)

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /home/devops/Python-MySQL
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and fill in your MySQL credentials:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=crud_db
   ```

5. **Set up the database**
   ```bash
   python setup_db.py
   ```

## Running the Application

1. **Start the Flask development server**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

2. **Test the API (optional)**
   In another terminal:
   ```bash
   python tests.py
   ```

## API Endpoints

### Health Check
- **GET** `/health` - Check if API is running

### Users Management

#### Create User
- **POST** `/users`
- **Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```

#### Get All Users
- **GET** `/users`

#### Get User by ID
- **GET** `/users/<id>`

#### Update User
- **PUT** `/users/<id>`
- **Body:**
  ```json
  {
    "name": "Updated Name",
    "email": "newemail@example.com",
    "age": 31
  }
  ```

#### Delete User
- **DELETE** `/users/<id>`

## Example Usage with cURL

```bash
# Create a user
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","age":30}'

# Get all users
curl http://localhost:5000/users

# Get a specific user
curl http://localhost:5000/users/1

# Update a user
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe","age":31}'

# Delete a user
curl -X DELETE http://localhost:5000/users/1
```

## Project Structure

```
Python-MySQL/
├── app.py              # Main Flask application with CRUD endpoints
├── setup_db.py         # Database initialization script
├── tests.py            # API testing script
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Environment variables (create from .env.example)
└── README.md          # This file
```

## Database Schema

The application uses a single `users` table with the following structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Error Handling

The API returns appropriate HTTP status codes:
- **200** - OK (successful GET, PUT)
- **201** - Created (successful POST)
- **400** - Bad Request (missing fields, duplicate email)
- **404** - Not Found (user doesn't exist)
- **500** - Internal Server Error

All error responses include a JSON error message.

## Technologies Used

- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database operations
- **mysql-connector-python** - MySQL database driver
- **python-dotenv** - Environment variable management

## License

MIT License
