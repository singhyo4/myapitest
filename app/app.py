from flask import Flask
from flask import request

app = Flask(__name__)

stores = [
    {
       "name": "mystore", 
       "items": [
         {  "name": "chair",
           "price": "$20"
         },
         {
           "name": "table",
            "price": "$30"  
         }
       ]   
    }
]

@app.get("/store")
def get_store():
    return {"stores": stores}

@app.post("/store")
def create_store():
    new_request = request.get_json()
    
        # Validate required fields
    if not all(key in new_request for key in ("name", "item_name", "price")):
        return {"error": "Missing fields in request"}, 400
    new_store = {"name":new_request["name"],
                  "items":
                      [
                          {
                            "name":new_request["item_name"],
                            "price":new_request["price"]
                            } 
                      ] 
                }
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/items")
def update_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["item_name"],
                        "price":request_data["price"]
                        }
            store["items"].append(new_item)
            return new_item
    return {"message": "store noot found"} , 400

@app.get("/store/<string:name>/items")
def get_item(name):
 #   request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_items = store["items"] 
            return new_items
    return {"message": "store noot found"} , 400

@app.get("/store/<string:name>")
def get_mystore(name):
#    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            return store["name"]
    return {"message": "store noot found"} , 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug= True)
    
    
