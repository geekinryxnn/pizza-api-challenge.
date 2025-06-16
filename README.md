# Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their relationships, built with Flask, SQLAlchemy, and Flask-Migrate.


## Features

- Manage restaurants and pizzas
- Associate pizzas with restaurants (with price)
- RESTful endpoints for CRUD operations
- Database migrations and seeding

## Project Structure

```
pizza-api-challenge.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   └── controllers/
│       ├── restaurant_controller.py
│       ├── pizza_controller.py
│       └── restaurant_pizza_controller.py
├── migrations/
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd pizza-api-challenge.
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables (optional):**
    - Create a `.env` file in the root directory and add:
      ```
      FLASK_APP=server.app
      FLASK_ENV=development
      ```

## Database Migrations

1. **Initialize migrations (first time only):**
    ```bash
    flask db init
    ```

2. **Generate a migration:**
    ```bash
    flask db migrate -m "Initial migration."
    ```

3. **Apply migrations:**
    ```bash
    flask db upgrade
    ```

## Seeding the Database

To populate the database with sample data:

```bash
python -m server.seed
```

## Running the Server

Start the Flask development server:

```bash
flask run
```
or
```bash
python -m server.app
```

The API will be available at [http://localhost:5000](http://localhost:5000).

## API Endpoints

> **Note:** Update this section with your actual endpoints and their usage.

### Restaurants

- `GET /restaurants` — List all restaurants
- `GET /restaurants/<id>` — Get a single restaurant
- `POST /restaurants` — Create a new restaurant
- `DELETE /restaurants/<id>` — Delete a restaurant

### Pizzas

- `GET /pizzas` — List all pizzas
- `POST /pizzas` — Create a new pizza

### Restaurant Pizzas

- `POST /restaurant_pizzas` — Associate a pizza with a restaurant (with price)

## Testing

> Add your testing instructions here if you have tests.

## Troubleshooting

- **ModuleNotFoundError:**  
  Always run scripts using the `-m` flag from the project root, e.g.:
  ```bash
  python -m server.seed
  ```
- **Database errors:**  
  Ensure you have run migrations and seeded the database.

