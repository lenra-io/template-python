def render(data, props):
    userData = data[0]
    
    return {
        "_type": "text",
        "value": userData
    }