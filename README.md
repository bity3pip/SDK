# SDK Challenge API

This project is a FastAPI-based application that serves as a bridge to the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API. It includes a custom SDK for fetching and creating posts, a service layer for business logic, and an in-memory storage system.

## Features

- **JSONPlaceholder SDK**: A simple wrapper around the JSONPlaceholder REST API.
- **Service Layer**: Handles data flow between the SDK and local storage.
- **In-Memory Storage**: Temporary storage for posts fetched or created during the session.
- **FastAPI Endpoints**: RESTful API to interact with the system.

## Project Structure

```text
.
├── app
│   ├── schemas         # Pydantic models for request/response
│   ├── sdk             # JSONPlaceholder SDK implementation
│   ├── service         # Business logic layer
│   └── storage         # In-memory data storage
├── tests               # Unit tests
├── main.py             # FastAPI application entry point
├── requirements.txt    # Project dependencies
└── pytest.ini          # Pytest configuration
```

## API Endpoints

- **GET `/fetch/{post_id}`**: Fetches a post from JSONPlaceholder and saves it to local storage.
- **GET `/fetch-recent`**: Fetches the most recent posts (default 5) and saves them locally.
- **GET `/posts/{post_id}`**: Retrieves a post from local storage.
- **GET `/posts`**: Lists all posts currently in local storage.
- **POST `/create`**: Creates a new post on JSONPlaceholder and saves it to local storage.

## Setup and Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python -m uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

3. **API Documentation**:
   Once the server is running, you can access the interactive Swagger UI at `http://localhost:8000/docs`.

## Running Tests

To run the project tests, use the following command:
```bash
pytest
```