import requests

def getDoc(api, coll, id) :
    return requests.get(api["url"] +"/app-api/v1/data/colls/"+coll+"/docs/"+id, headers = headers(api))
    
def createDoc(api, coll, doc) :
    return requests.post(api["url"] +"/app-api/v1/data/colls/"+coll+"/docs", json = doc, headers = headers(api))
    
def updateDoc(api, coll, doc) :
    return requests.put(api["url"] +"/app-api/v1/data/colls/"+coll+"/docs/" + doc["_id"], json = doc, headers = headers(api))
    
def deleteDoc(api, coll, doc) :
    return requests.delete(api["url"] +"/app-api/v1/data/colls/"+coll+"/docs/"+doc["_id"], headers = headers(api))
    
def find(api, coll, query) :
    return requests.post(api["url"] +"/app-api/v1/data/colls/"+coll+"/find", json = query, headers = headers(api))
    
def updateMany(api, coll, filter, update) :
    return requests.post(api["url"] +"/app-api/v1/data/colls/"+coll+"/updateMany", json = {
        'filter': filter,
        'update': update
    }, headers = headers(api))
    

def headers(api) :
    return { "Authorization": "Bearer "+ api["token"] }