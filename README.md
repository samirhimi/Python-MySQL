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
   - Copy `.env.example` from `python_apps/` to `.env`
   ```bash
   cp python_apps/.env.example python_apps/.env
   ```
   - Edit `python_apps/.env` and fill in your MySQL credentials:
   ```
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DATABASE=crud_db
   ```

5. **Set up the database**
   ```bash
   python python_apps/setup_db.py
   ```

## Running the Application

1. **Start the Flask development server**
   ```bash
   python python_apps/app.py
   ```
   The API will be available at `http://localhost:5000`

2. **Test the API (optional)**
   In another terminal:
   ```bash
   python python_apps/tests.py
   ```

## Code Quality & Security

This project includes automated checks for code security, linting, and formatting.

### Local Development Checks

Run these commands locally before committing:

```bash
# Run all linting and security checks
black python_apps/          # Format code
isort python_apps/          # Sort imports
flake8 python_apps/         # Lint code
pylint python_apps/         # Code analysis
bandit -r python_apps/      # Security scan
safety check                # Check dependencies for vulnerabilities
```

### Automatic CI/CD Checks

A GitHub Actions workflow automatically runs on every push and pull request:

- **Bandit**: Security issue scanner
- **Safety**: Dependency vulnerability checker
- **Black**: Code formatter verification
- **isort**: Import sorting verification
- **Flake8**: Style guide enforcement and linting
- **Pylint**: Code quality analysis

**Supported Python Versions**: 3.9, 3.10, 3.11

The workflow is defined in [.github/workflows/security-lint.yml](.github/workflows/security-lint.yml)

### Configuration Files

- `.flake8` - Flake8 linting configuration
- `.pylintrc` - Pylint configuration
- `pyproject.toml` - Black, isort, and Bandit configuration

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
├── .github/
│   └── workflows/
│       └── security-lint.yml    # GitHub Actions CI/CD workflow
├── python_apps/
│   ├── app.py                   # Main Flask application with CRUD endpoints
│   ├── setup_db.py              # Database initialization script
│   ├── tests.py                 # API testing script
│   └── .env.example             # Example environment variables
├── .flake8                       # Flake8 linting configuration
├── .gitignore                    # Git ignore rules
├── .pylintrc                     # Pylint configuration
├── pyproject.toml                # Black, isort, and tool configurations
├── requirements.txt              # Python dependencies (dev + production)
└── README.md                     # This file
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
