from app import app
from flask import jsonify
from flask import flash, request
import json

inventories = [{"itemId":"EST-1","qty":"10000"}, {"itemId":"EST-2","qty":"10000"}, {"itemId":"EST-3","qty":"10000"}, {"itemId":"EST-4","qty":"10000"}, {"itemId":"EST-5","qty":"10000"}, {"itemId":"EST-6","qty":"10000"}, {"itemId":"EST-7","qty":"10000"}, {"itemId":"EST-8","qty":"10000"}, {"itemId":"EST-9","qty":"10000"}, {"itemId":"EST-10","qty":"10000"}, {"itemId":"EST-11","qty":"10000"}, {"itemId":"EST-12","qty":"10000"}, {"itemId":"EST-13","qty":"10000"}, {"itemId":"EST-14","qty":"10000"}, {"itemId":"EST-15","qty":"10000"}, {"itemId":"EST-16","qty":"10000"}, {"itemId":"EST-17","qty":"10000"}, {"itemId":"EST-18","qty":"10000"}, {"itemId":"EST-19","qty":"10000"}, {"itemId":"EST-20","qty":"10000"}, {"itemId":"EST-21","qty":"10000"}, {"itemId":"EST-22","qty":"10000"}, {"itemId":"EST-23","qty":"10000"}, {"itemId":"EST-24","qty":"10000"}, {"itemId":"EST-25","qty":"10000"}, {"itemId":"EST-26","qty":"10000"}, {"itemId":"EST-27","qty":"10000"}, {"itemId":"EST-28","qty":"10000"}]

# Use GET requests to retrieve resource representation/information only
@app.route('/inventories', methods=['GET'])
def findAll():
    try:
        respone = jsonify(inventories)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e) 

# Use GET requests to retrieve resource representation/information only
@app.route('/inventories/<id>', methods=['GET'])
def findOne(id):
    try:
        one = find(id)
        if(one):
            respone = jsonify(one)
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)

# Use POST APIs to create new subordinate resources
@app.route('/inventories', methods=['POST'])
def add_inv():
    try:
        #new = {"itemId":"WST-99","qty":"100"}
        _json = request.json
        _itemId = _json['itemId']
        _qty = _json['qty']
        new = {"itemId": _itemId ,"qty": _qty}

        one = find(_itemId) 

        if one == None:
            inventories.append(new)

            respone = jsonify(inventories)
            respone.status_code = 200
            return respone
        else:
            return duplicate_found()
    except Exception as e:
        print(e)

# DELETE APIs are used to delete resources
@app.route('/inventories/<id>', methods=['DELETE'])
def del_inv(id):
    try:        
        one = find(id) 
        
        if one == None:
            return not_found()

        remove(id)

        respone = jsonify(inventories)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)

# Use PUT APIs primarily to update existing resource
@app.route('/inventories/<id>', methods=['PUT'])
def upd_inv(id):
    try:        
        one = find(id)         
        if one == None:
            return not_found()


        _json = request.json
        _itemId = _json['itemId']
        _qty = _json['qty']
        new = {"itemId": _itemId ,"qty": _qty}
        
        remove(id)        
        inventories.append(new)

        respone = jsonify(inventories)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone    

@app.errorhandler(409)
def duplicate_found(error=None):
    message = {
        'status': 409,
        'message': 'Duplicate resource or resource already exists. : ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone    


def find(key):
    for i in inventories:
        if(i['itemId'] == key):
            print(i['itemId']," ",key)
            return i

def remove(key):
    for i in range(len(inventories)):
        if inventories[i]['itemId'] == key:
            del inventories[i]
            break

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
