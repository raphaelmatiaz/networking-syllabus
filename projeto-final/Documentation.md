1. Accessing the App
The Frontend:
Open a browser and go to http://localhost.
This will display the HTML page where you can interact with the API endpoints (GET, POST, PUT, DELETE) via the form.

The API Backend:
The API itself can be accessed directly at http://localhost/api, but it’s more user-friendly to use the frontend for interactions.

2. Using the API Endpoints
Here’s how the CRUD endpoints work:

Base URL
The API is proxied through NGINX at http://localhost/api.

Endpoints
Method	Endpoint	Description	Request Body (JSON)
GET	/items/{item_id}	Retrieve item details by ID.	None
POST	/items/?item_id={id}	Create a new item.	{ "name": "...", "description": "...", "price": 0.0, "quantity": 0 }
PUT	/items/{item_id}	Update an item by ID.	{ "name": "...", "description": "...", "price": 0.0, "quantity": 0 }
DELETE	/items/{item_id}	Delete an item by ID.	None
3. Interacting via the Frontend
Open your browser to http://localhost.
Fill out the form fields:
Item ID: Specify the ID for the item.
Name, Description, Price, Quantity: Use these fields for POST or PUT requests.
Click the respective button for the operation you want to perform:
Create Item (POST)
Get Item (GET)
Update Item (PUT)
Delete Item (DELETE)
Results will be displayed in an alert dialog, showing the server response.
4. Testing the API Endpoints
If you prefer to test the API directly (without the frontend), you can use tools like Postman, curl, or a browser’s REST client.

Example with curl:
Create an Item (POST):

bash
Copiar código
curl -X POST http://localhost/api/items/?item_id=1 \
-H "Content-Type: application/json" \
-d '{"name": "Sword", "description": "A sharp blade", "price": 10.99, "quantity": 2}'
Get an Item (GET):

bash
Copiar código
curl -X GET http://localhost/api/items/1
Update an Item (PUT):

bash
Copiar código
curl -X PUT http://localhost/api/items/1 \
-H "Content-Type: application/json" \
-d '{"name": "Shield", "description": "A sturdy shield", "price": 15.99, "quantity": 1}'
Delete an Item (DELETE):

bash
Copiar código
curl -X DELETE http://localhost/api/items/1
5. Documentation
Project Overview
This project demonstrates a CRUD API using FastAPI and serves a frontend for user interaction, with NGINX acting as a load balancer.

Features
REST API for basic CRUD operations.
Simple HTML frontend for API interaction.
NGINX as a load balancer for the backend.
How to Run
Start the project:
bash
Copiar código
docker-compose up --build
Access the application:
Frontend: http://localhost
API: http://localhost/api
API Reference
Base URL: http://localhost/api
GET /items/{item_id}
Retrieves an item by its ID.

POST /items/?item_id={id}
Creates a new item. Example body:

json
Copiar código
{
  "name": "Item Name",
  "description": "Item Description",
  "price": 0.0,
  "quantity": 1
}
PUT /items/{item_id}
Updates an item. Example body:

json
Copiar código
{
  "name": "Updated Name",
  "description": "Updated Description",
  "price": 1.99,
  "quantity": 10
}
DELETE /items/{item_id}
Deletes an item by its ID.

Known Issues
Ensure all services are running (frontend, backend, nginx).
Check the docker-compose logs if there are any errors.
