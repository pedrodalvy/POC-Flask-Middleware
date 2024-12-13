# POC Flask Middleware

A Proof of Concept (POC) project to demonstrate the implementation and usage of middleware in the Flask framework.

## 🚀 Summary

- **Middleware Integration**: Demonstrates how middleware can intercept and process requests and responses in Flask.
- **CRUD Endpoints**: Implements Create, Read, Read by ID, Update, and Delete operations.
- **Logging Mechanism**: Logs request and response data to the terminal for each endpoint.
- **Example Requests**: Provides example HTTP requests in `requests/routes.http`.
- **Simple Setup**: Utilizes Poetry for dependency management and application execution.

## 📁 Project Structure

```
poc-flask-middleware/
├── poetry.lock               # Poetry lock file with resolved dependencies
├── pyproject.toml            # Poetry configuration and dependencies
├── README.md                 # Project documentation
├── requests/
│   └── routes.http           # Example HTTP requests for testing
└── src/
    ├── app.py                # Initializes the Flask app and middleware
    ├── __init__.py           # Application package initializer
    ├── middlewares.py        # Middleware implementation for logging
    └── routes.py             # Defines CRUD endpoints
```

- **poetry.lock**: Ensures consistent dependency versions across environments.
- **pyproject.toml**: Specifies project dependencies and Poetry configurations.
- **requests/routes.http**: Contains example HTTP requests to interact with the application's endpoints.
- **src/**: Contains the main application source code.
    - **app.py**: Sets up the Flask application and registers middleware.
    - **middlewares.py**: Implements middleware for logging requests and responses.
    - **routes.py**: Defines CRUD endpoints (create, read, read_by_id, update, delete).

## 🚀 Getting Started

### 📝 Prerequisites

- **Python 3.13+**
- **Poetry** package manager

### 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:pedrodalvy/poc-flask-middleware.git
   cd poc-flask-middleware
   ```

2. **Install Poetry**

   If you don't have Poetry installed, follow the [official installation guide](https://python-poetry.org/docs/#installation).

3. **Install dependencies**

   ```bash
   poetry shell
   poetry install
   ```

### 🚀 Running the Application

Start the Flask application using Poetry:

```bash
poetry run start [--debug]
```

- `--debug`: Optional flag to run the application in debug mode.

The application will start on `http://127.0.0.1:5000/`.

## 🔍 Example Usage

### 📄 Available Endpoints

| Method | Endpoint  | Description               |
|--------|-----------|---------------------------|
| POST   | `/create` | Create a new resource     |
| GET    | `/`       | Retrieve all resources    |
| GET    | `/<id>`   | Retrieve a resource by ID |
| PUT    | `/<id>`   | Update a resource by ID   |
| DELETE | `/<id>`   | Delete a resource by ID   |

### 🛠️ Example Requests

Refer to `requests/routes.http` for example HTTP requests.

## 🛠️ Additional Notes

- **Logging in Production**: The current logging mechanism is for demonstration purposes only. For production environments, consider using robust logging libraries like `logging` with proper log levels and handlers.
- **Extending Functionality**: You can add more middleware components for tasks such as authentication, rate limiting, or error handling.
- **Example Requests**: Use the `requests/routes.http` file to explore and test the application's endpoints.
- **Contributing**: Contributions are welcome! Please open issues or submit pull requests for enhancements or bug fixes.
