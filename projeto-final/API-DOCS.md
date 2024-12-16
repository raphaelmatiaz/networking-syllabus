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
curl -X POST http://localhost/api/items/?item_id=1 \
-H "Content-Type: application/json" \
-d '{"name": "Sword", "description": "A sharp blade", "price": 10.99, "quantity": 2}'
Get an Item (GET):

bash
curl -X GET http://localhost/api/items/1
Update an Item (PUT):

bash
curl -X PUT http://localhost/api/items/1 \
-H "Content-Type: application/json" \
-d '{"name": "Shield", "description": "A sturdy shield", "price": 15.99, "quantity": 1}'
Delete an Item (DELETE):

bash
curl -X DELETE http://localhost/api/items/1