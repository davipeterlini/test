# Python Backend API

This is a simple Python backend API built using Flask. It provides basic CRUD operations for managing an in-memory list of items.

## Features

- **GET /items**: Retrieve all items.
- **POST /items**: Add a new item.
- **DELETE /items/<item_id>**: Delete an item by its ID.

## Requirements

- Python 3.7 or higher
- Flask

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the API at `http://127.0.0.1:5000`.

## Example Usage

### Add an Item
```bash
curl -X POST -H "Content-Type: application/json" -d '{"item": "Sample Item"}' http://127.0.0.1:5000/items
```

### Get All Items
```bash
curl http://127.0.0.1:5000/items
```

### Delete an Item
```bash
curl -X DELETE http://127.0.0.1:5000/items/0
```

## Notes

- This is a simple in-memory API. Data will be lost when the server restarts.
- For production use, consider using a database and deploying with a production-ready server like Gunicorn.

## License

This project is licensed under the MIT License.