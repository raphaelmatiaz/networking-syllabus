from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# In-memory database substitute
items = {}

# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int

# GET endpoint
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    return {"item_id": item_id, "item": items[item_id]}

# POST endpoint
@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Item ID already exists"
        )
    items[item_id] = item
    return {"message": "Item created", "item": item}

# PUT endpoint
@app.put("/items/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    items[item_id] = item
    return {"message": "Item updated", "item": item}

# DELETE endpoint
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    del items[item_id]
    return {"message": "Item deleted"}



# Step 3: Explanation of the API Endpoints

# GET /items/{item_id}
# Retrieves an item by its item_id.
# Returns 200 OK if the item is found.
# Returns 404 Not Found if the item doesn't exist.


# POST /items/
# Creates a new item with the provided item_id and Item payload.
# Returns 201 Created if successful.
# Returns 400 Bad Request if the item_id already exists.


# PUT /items/{item_id}
# Updates an existing item identified by item_id.
# Returns 200 OK if the item is updated.
# Returns 404 Not Found if the item doesn't exist.


# DELETE /items/{item_id}
# Deletes the item identified by item_id.
# Returns 204 No Content on success.
# Returns 404 Not Found if the item doesn't exist.


#run the application: uvicorn main:app --reload
