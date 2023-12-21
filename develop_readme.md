# To-Do List API

This project is a RESTful API built with Django and Django REST Framework. It allows users to manage their to-do items, including creating, updating, and deleting tasks. Each task can have a title, description, completion status, creation and update timestamps, due date, priority, and associated tags. The API also supports user management, with each user having their own set of tasks and tags.

## Prerequisites

You will need to have Python 3.10 or higher and Docker installed. You will also need a copy of the source code, which you can obtain by cloning the GitHub repository.

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/RDSDeveloper/todo-challenge
    ```
2. Navigate into the directory:
    ```
    cd todo-list-api
    ```
3. Copy the `env.sample` file to a new file named `.env`:
    ```
    cp env.sample .env
    ```
4. Open the `.env` file and replace the placeholder values with your actual data.

### Running the Application

1. Build and start the Docker containers:
    ```
    docker-compose up --build
    ```
    This command will install the necessary dependencies as defined in the `requirements.txt` file and start the application.

### API Endpoints

Once the application is running, you can access the following endpoints:

#### Authentication and Registration

- `http://localhost:8000/dj-rest-auth/login/`: Log in.
- `http://localhost:8000/dj-rest-auth/logout/`: Log out.
- `http://localhost:8000/dj-rest-auth/password/reset/`: Reset password.
- `http://localhost:8000/dj-rest-auth/registration/`: Register as a new user.

#### Todos

- `http://localhost:8000/api/todos/`: List all todos or create a new one.
- `http://localhost:8000/api/todos/<id>/`: Retrieve, update, or delete a specific todo.

#### Tags

- `http://localhost:8000/api/tags/`: List all tags or create a new one.
- `http://localhost:8000/api/tags/<id>/`: Retrieve, update, or delete a specific tag.

#### API Documentation

- `http://localhost:8000/api/schema/`: View the API schema.
- `http://localhost:8000/api/schema/redoc`: View the API documentation in Redoc.
- `http://localhost:8000/api/schema/swagger-ui/`: View the API documentation in Swagger UI.

Replace `<id>` with the ID of the todo or tag you want to retrieve, update, or delete.

## Endpoint Details

### List all todos or create a new one

- **URL**: `http://localhost:8000/api/todos/`
- **HTTP Method**: GET, POST
- **Input Parameters (POST)**:
    - `title`: String (max 200 characters), required
    - `description`: String, optional
    - `completed`: Boolean, optional
    - `due_date`: DateTime, optional
    - `priority`: String (one of "H", "M", "L"), optional
    - `tags`: List of strings (names of existing tags), optional

### Retrieve, update, or delete a specific todo

- **URL**: `http://localhost:8000/api/todos/<id>/`
- **HTTP Method**: GET, PUT, DELETE
- **Input Parameters (PUT)**:
    - `title`: String (max 200 characters), optional
    - `description`: String, optional
    - `completed`: Boolean, optional
    - `due_date`: DateTime, optional
    - `priority`: String (one of "H", "M", "L"), optional
    - `tags`: List of strings (names of existing tags), optional

### List all tags or create a new one

- **URL**: `http://localhost:8000/api/tags/`
- **HTTP Method**: GET, POST
- **Input Parameters (POST)**:
    - `name`: String (max 200 characters), required

### Retrieve, update, or delete a specific tag

- **URL**: `http://localhost:8000/api/tags/<id>/`
- **HTTP Method**: GET, PUT, DELETE
- **Input Parameters (PUT)**:
    - `name`: String (max 200 characters), optional

### Test User

To test the API, you can create your own user using the registration endpoint:

- `http://localhost:8000/dj-rest-auth/registration/`

After registering, you can log in with your new user credentials at the login endpoint:

- `http://localhost:8000/dj-rest-auth/login/`

Once logged in, you can use this user to test the API endpoints.

### Testing

This project uses Django's built-in testing tools in combination with Coverage.py. To run the tests and generate a coverage report, use the following commands:

1. Run the tests:
    ```
    docker-compose run web coverage run manage.py test
    ```
2. Generate the coverage report:
    ```
    docker-compose run web coverage report
    ```

This will display a report in the terminal showing the coverage of each file.

If you want to generate an HTML report, you can use the following command instead:

1. Generate the coverage report as HTML:
    ```
    docker-compose run web coverage html
    ```

This will generate an HTML report in a new `htmlcov` directory. You can open the `index.html` file in your web browser to view the report.

