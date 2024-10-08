from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": 'My Store',
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")  # http://127.0.0.1/store
def get_stores():
    return {"stores": stores}

@app.post("/store") # http://127.0.0.1/store
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"], 
        "items": []
        }
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")    # http://127.0.0.1/store/<name>
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")    # http://127.0.0.1/store/<name>
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/<string:req_item>")    # http://127.0.0.1/store/<name>/<item>
def get_item(name, req_item):
    for store in stores:
        if store["name"] == name:
            for item in store["items"]:
                if item["name"] == req_item:
                    return item
    return {"message": "Item not found"}, 404