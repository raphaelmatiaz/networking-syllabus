# CRUD API with FastAPI

## Project Overview
This project demonstrates a CRUD API built with FastAPI, providing a frontend for user interaction. It uses NGINX as a load balancer and reverse proxy to streamline request handling and service communication.

## Features
- **REST API** for basic CRUD operations.
- **HTML Frontend** for interacting with the API.
- **NGINX Load Balancer** for the backend (API) with CIDR for each subnet.
- **NGINX Reverse Proxy** to upstream requests to frontend and backend services.
- **HTTPS** for secure encrypted requests.
- **SSL Certificate** To encrypt and decrypt requests.

## How to Run
1. Start the project:
   ```bash
   make up
   ```
2. Access the application:
   - **Frontend**: [http://localhost](http://localhost)
   - **API**: [http://localhost/api](http://localhost/api)

## API Reference

### Base URL
`http://localhost/api`

### Endpoints

#### GET `/items/{item_id}`
Retrieves an item by its ID.

#### POST `/items/?item_id={id}`
Creates a new item.

**Example Request Body:**
```json
{
  "name": "Item Name",
  "description": "Item Description",
  "price": 0.0,
  "quantity": 1
}
```

#### PUT `/items/{item_id}`
Updates an item.

**Example Request Body:**
```json
{
  "name": "Updated Name",
  "description": "Updated Description",
  "price": 1.99,
  "quantity": 10
}
```

#### DELETE `/items/{item_id}`
Deletes an item by its ID.

## Known Issues
- Ensure all services are running (frontend, backend, NGINX).
- Check the `docker-compose` logs if any errors occur.

