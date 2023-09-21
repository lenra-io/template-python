def render(data, counter) :
  return {
    "_type": "flex",
    "spacing": 16,
    "mainAxisAlignment": "spaceEvenly",
    "crossAxisAlignment": "center",
    "children": [
      {
        "_type": "text",
        "value": counter["text"] +": "+ str(data[0]["count"])
      },
      {
        "_type": "button",
        "text": "+",
        "onPressed": {
          "_type": "listener",
          "name": "increment",
          "props": {
            "id": data[0]["_id"],
          }
        }
      }
    ]
  }