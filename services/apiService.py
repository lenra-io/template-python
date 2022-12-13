import requests

def getDoc(api, coll, id) :
    return requests.get(api["url"] +"/app/colls/"+coll+"/docs/"+id, headers = headers(api))
    
def createDoc(api, coll, doc) :
    return requests.post(api["url"] +"/app/colls/"+coll+"/docs", json = doc, headers = headers(api))
    
def updateDoc(api, coll, doc) :
    return requests.put(api["url"] +"/app/colls/"+coll+"/docs/" + doc["_id"], json = doc, headers = headers(api))
    
def deleteDoc(api, coll, doc) :
    return requests.delete(api["url"] +"/app/colls/"+coll+"/docs/"+doc["_id"], headers = headers(api))
    
def executeQuery(api, coll, query) :
    return requests.post(api["url"] +"/app/colls/"+coll+"/docs/find", json = query, headers = headers(api))
    

def headers(api) :
    return { "Authorization": "Bearer "+ api["token"] }