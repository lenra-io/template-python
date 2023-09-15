def render(data, counter) :
    return {
        "_type": "flex",
        "direction": "vertical",
        "spacing": 16,
        "mainAxisAlignment": "spaceEvenly",
        "crossAxisAlignment": "center",
        "children": [
            {
                "_type": "view",
                "name": "counter",
                "find": {
                    "coll": "counter",
                    "query": {
                        "user": "@me"
                    }
                },
                "props": { "text": "My personnal counter" }
            },
            {
                "_type": "view",
                "name": "counter",
                "find": {
                    "coll": "counter",
                    "query": {
                        "user": "global"
                    }
                },
                "props": { "text": "The common counter" }
            }
        ]
    }